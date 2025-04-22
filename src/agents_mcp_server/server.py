"""
Octagon Investor Agents MCP server.

This module provides a FastMCP server that exposes investor agents augmented with Octagon's private market data through the Model Context Protocol.
"""

import asyncio
from typing import Any, Dict, Optional
from pathlib import Path

from agents import Agent, Runner, trace, OpenAIResponsesModel
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

from agents_mcp_server.cli import octagon_client

ALFRED_LIN_PROFILE = (Path(__file__).parent / "investors/alfred_lin.md").read_text()
BILL_GURLEY_PROFILE = (Path(__file__).parent / "investors/bill_gurley.md").read_text()
FRED_WILSON_PROFILE = (Path(__file__).parent / "investors/fred_wilson.md").read_text()
JOSH_KOPELMAN_PROFILE = (Path(__file__).parent / "investors/josh_kopelman.md").read_text()
KEITH_RABOIS_PROFILE = (Path(__file__).parent / "investors/keith_rabois.md").read_text()
MARK_ANDREESEN_PROFILE = (Path(__file__).parent / "investors/mark_andreessen.md").read_text()
PETER_THIEL_PROFILE = (Path(__file__).parent / "investors/peter_thiel.md").read_text()
REID_HOFFMAN_PROFILE = (Path(__file__).parent / "investors/reid_hoffman.md").read_text()


mcp = FastMCP(
    name="OpenAI Agents",
    instructions="""This MCP server provides access to Investor agents through the Model Context Protocol.""",
)

class AgentResponse(BaseModel):
    """Response from an OpenAI agent."""

    response: str = Field(..., description="The response from the agent")
    raw_response: Optional[Dict[str, Any]] = Field(
        None, description="The raw response data from the agent, if available"
    )


# --- Octagon Private Market Agents (Usage Examples) ---
# octagon_companies_agent = Agent(
#     name="Companies Agent",
#     instructions="Retrieve detailed company information from Octagon's companies database.",
#     model=OpenAIResponsesModel(model="octagon-companies-agent", openai_client=octagon_client),
#     tools=[],
# )

# octagon_funding_agent = Agent(
#     name="Funding Agent",
#     instructions="Retrieve detailed funding information from Octagon's companies database.",
#     model=OpenAIResponsesModel(model="octagon-funding-agent", openai_client=octagon_client),
#     tools=[],
# )

# octagon_investors_agent = Agent(
#     name="Investors Agent",
#     instructions="Retrieve detailed investor information from Octagon's investors database.",
#     model=OpenAIResponsesModel(model="octagon-investors-agent", openai_client=octagon_client),
#     tools=[],
# )


# --- Octagon Alfred Lin Agent ---
@mcp.tool(
    name="octagon-alfred-lin-agent",
    description="Alfred Lin - First Round Capital partner. Focuses on early-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)
async def alfred_lin_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        alfred_agent = Agent(
            name="Alfred Lin Orchestrator",
            instructions=ALFRED_LIN_PROFILE,
            tools=[],
        )

        with trace("Alfred Lin analysis"):
            result = await Runner.run(alfred_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Alfred Lin", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:
        print(f"Error in Alfred Lin Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Alfred Lin's analysis: {str(e)}",
            raw_response=None
        )
    

# --- Octagon Bill Gurley Agent ---
@mcp.tool(
    name="octagon-bill-gurley-agent",
    description="Bill Gurley - Benchmark Capital partner. Focuses on late-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)
async def bill_gurley_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        bill_agent = Agent(
            name="Bill Gurley Orchestrator",
            instructions=BILL_GURLEY_PROFILE,
            tools=[],
        )

        with trace("Bill Gurley analysis"):
            result = await Runner.run(bill_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Bill Gurley", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:
        print(f"Error in Bill Gurley Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Bill Gurley's analysis: {str(e)}",
            raw_response=None
        )
    

# --- OctagonFred Wilson Agent ---
@mcp.tool(
    name="octagon-fred-wilson-agent",
    description="Fred Wilson - Union Square Ventures co-founder & veteran early-stage investor. Brings 30+ years experience evaluating community-driven networks, founder-first philosophies, and disruptive market platforms. Ask me about network effects, startup ecosystems, or building with purpose.",
)
async def fred_wilson_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
    
        fred_agent = Agent(
            name="Fred Wilson Orchestrator",
            instructions=FRED_WILSON_PROFILE,
            tools=[],
        )

        with trace("Fred analysis"):
            result = await Runner.run(fred_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Fred Wilson", "items": [str(item) for item in result.new_items]},
        )

    except Exception as e:
        print(f"Error in Fred Wilson Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Fred's analysis: {str(e)}",
            raw_response=None
        )
    

# --- Octagon Josh Kopelman Agent ---
@mcp.tool(
    name="octagon-josh-kopelman-agent",
    description="Josh Kopelman - First Round Capital partner. Focuses on early-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)
async def josh_kopelman_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        josh_agent = Agent(
            name="Josh Kopelman Orchestrator",
            instructions=JOSH_KOPELMAN_PROFILE,
            tools=[],
        )

        with trace("Josh Kopelman analysis"):
            result = await Runner.run(josh_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Josh Kopelman", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:
        print(f"Error in Josh Kopelman Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Josh's analysis: {str(e)}",
            raw_response=None
        )
    

# --- Octagon Keith Rabois Agent ---
@mcp.tool(
    name="octagon-keith-rabois-agent",
    description="Keith Rabois - Khosla Ventures partner. Focuses on late-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)   
async def keith_rabois_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        keith_agent = Agent(
            name="Keith Rabois Orchestrator",   
            instructions=KEITH_RABOIS_PROFILE,
            tools=[],
        )

        with trace("Keith Rabois analysis"):
            result = await Runner.run(keith_agent, query)   

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Keith Rabois", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:  
        print(f"Error in Keith Rabois Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Keith's analysis: {str(e)}",
            raw_response=None
        )
    

# --- Octagon Mark Andreessen Agent ---
@mcp.tool(
    name="octagon-mark-andreessen-agent",
    description="Mark Andreessen - Andreessen Horowitz partner. Focuses on late-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)
async def mark_andreessen_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        mark_agent = Agent(
            name="Mark Andreessen Orchestrator",
            instructions=MARK_ANDREESEN_PROFILE,
            tools=[],
        )

        with trace("Mark Andreessen analysis"):
            result = await Runner.run(mark_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Mark Andreessen", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:
        print(f"Error in Mark Andreessen Orchestrator: {e}")    
        return AgentResponse(
            response=f"An error occurred while processing Mark's analysis: {str(e)}",
            raw_response=None
        )



# --- Octagon Peter Thiel Agent ---
@mcp.tool(
    name="octagon-peter-thiel-agent",
    description="Peter Thiel - Venture capitalist & 'Zero to One' author. Analyzes investments through the lens of monopoly theory, long-term thinking, and contrarian innovation. Ask me about technology breakthroughs, market-defining companies, or why competition is for losers.",
)
async def peter_thiel_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        
    
        peter_agent = Agent(
            name="Peter Thiel Orchestrator",
            instructions=PETER_THIEL_PROFILE,
            tools=[],
        )

        with trace("Peter analysis"):
            result = await Runner.run(peter_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Peter Thiel", "items": [str(item) for item in result.new_items]},
        )

    except Exception as e:
        print(f"Error in Peter Thiel Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Peter's analysis: {str(e)}",
            raw_response=None
        )
    

# --- Octagon Reid Hoffman Agent ---
@mcp.tool(
    name="octagon-reid-hoffman-agent",
    description="Reid Hoffman - Greylock Partners partner. Focuses on late-stage startups, with a keen eye for market trends and founder potential. Ask me about market-defining companies, disruptive technologies, or the next big thing.",
)
async def reid_hoffman_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        reid_agent = Agent(
            name="Reid Hoffman Orchestrator",
            instructions=REID_HOFFMAN_PROFILE,
            tools=[],
        )

        with trace("Reid Hoffman analysis"):
            result = await Runner.run(reid_agent, query)

        return AgentResponse(
            response=result.final_output,
            raw_response={"source": "Reid Hoffman", "items": [str(item) for item in result.new_items]},
        )
    except Exception as e:
        print(f"Error in Reid Hoffman Orchestrator: {e}")
        return AgentResponse(
            response=f"An error occurred while processing Reid's analysis: {str(e)}",
            raw_response=None
        )