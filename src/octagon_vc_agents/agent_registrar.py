
from typing import Callable
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP
from agents import Runner, trace, ItemHelpers, MessageOutputItem, Agent

class AgentResponse(BaseModel):
    response: str

class AgentRegistrar:
    def __init__(self, mcp: FastMCP):
        self.mcp = mcp

    def register(
        self,
        *,
        name: str,
        description: str,
        build_agent: Callable[[], object],
        vc_agent: bool = False,
        has_field_description: bool = False,
        octagon_activated: bool = False
    ):
        """
        Registers an agent as an MCP tool.

        Args:
            name (str): Display name of the agent (used in tool name).
            description (str): Description shown in the tool.
            build_agent (Callable): Function that returns an initialized Agent.
            traced (bool): Whether to wrap the agent run in a tracing context.
            has_field_description (bool): Whether to apply a field-level description to the input.
        """
        agent = build_agent()
        tool_name = f"octagon-{name.lower().replace(' ', '-')}-agent"

        # Conditionally define the tool with or without input field metadata
        if has_field_description:
            @self.mcp.tool(name=tool_name, description=description)
            async def _tool(query: str = Field(..., description="Investment-related question or query.")) -> AgentResponse:
                return await self._run_agent(agent, query, name, vc_agent)
        else:
            @self.mcp.tool(name=tool_name, description=description)
            async def _tool(query: str) -> AgentResponse:
                return await self._run_agent(agent, query, name, vc_agent)

    async def _run_agent(self, agent, query: str, name: str, vc_agent: bool) -> AgentResponse:
        try:
            if vc_agent:
                with trace(f"{name} analysis"):
                    # Agent runs first, fetching data internally via tools
                    orchestrator_result = await Runner.run(agent, query)

                    # Capture interim outputs (stock data fetched)
                    for item in orchestrator_result.new_items:
                        if isinstance(item, MessageOutputItem):
                            text = ItemHelpers.text_message_output(item)
                            if text:
                                print(f"  - Data fetched: {text}")
                    
                    final_output = orchestrator_result.final_output
            else:
                # Regular agent execution without orchestration
                result = await Runner.run(agent, query)
                final_output = result.final_output

            return AgentResponse(response=final_output)

        except Exception as e:
            return AgentResponse(response=str(e))

