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

FRED_WILSON_PROFILE = (Path(__file__).parent / "investors/fred_wilson.md").read_text()
PETER_THIEL_PROFILE = (Path(__file__).parent / "investors/peter_thiel.md").read_text()


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


# --- Octagon Private Market Agents (shared across Investors) ---
octagon_companies_agent = Agent(
    name="Companies Agent",
    instructions="Retrieve detailed company information from Octagon's companies database.",
    model=OpenAIResponsesModel(model="octagon-companies-agent", openai_client=octagon_client),
    tools=[],
)

octagon_funding_agent = Agent(
    name="Funding Agent",
    instructions="Retrieve detailed funding information from Octagon's companies database.",
    model=OpenAIResponsesModel(model="octagon-funding-agent", openai_client=octagon_client),
    tools=[],
)

octagon_investors_agent = Agent(
    name="Investors Agent",
    instructions="Retrieve detailed investor information from Octagon's investors database.",
    model=OpenAIResponsesModel(model="octagon-investors-agent", openai_client=octagon_client),
    tools=[],
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
        with trace("Fetch company data for Fred"):
            company_result = await Runner.run(octagon_companies_agent, query)
            company_info = company_result.final_output

        with trace("Fetch funding data for Fred"):
            funding_result = await Runner.run(octagon_funding_agent, query)
            funding_info = funding_result.final_output

        with trace("Fetch investor data for Fred"):
            investor_result = await Runner.run(octagon_investors_agent, query)
            investor_info = investor_result.final_output

        combined_context = f"""
            Company Info:
            {company_info}

            Funding Info:
            {funding_info}

            Investor Info:
            {investor_info}

            Query:
            {query}
        """

        fred_agent = Agent(
            name="Fred Wilson Orchestrator",
            instructions=FRED_WILSON_PROFILE,
            tools=[],
        )

        with trace("Fred analysis"):
            result = await Runner.run(fred_agent, combined_context)

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


# --- OctagonPeter Thiel Agent ---
@mcp.tool(
    name="octagon-peter-thiel-agent",
    description="Peter Thiel - Venture capitalist & 'Zero to One' author. Analyzes investments through the lens of monopoly theory, long-term thinking, and contrarian innovation. Ask me about technology breakthroughs, market-defining companies, or why competition is for losers.",
)
async def peter_thiel_orchestrator(
    query: str = Field(..., description="The investment-related question or query."),
) -> AgentResponse:
    try:
        with trace("Fetch company data for Peter"):
            company_result = await Runner.run(octagon_companies_agent, query)
            company_info = company_result.final_output

        with trace("Fetch funding data for Peter"):
            funding_result = await Runner.run(octagon_funding_agent, query)
            funding_info = funding_result.final_output

        with trace("Fetch investor data for Peter"):
            investor_result = await Runner.run(octagon_investors_agent, query)
            investor_info = investor_result.final_output

        combined_context = f"""
            Company Info:
            {company_info}

            Funding Info:
            {funding_info}

            Investor Info:
            {investor_info}

            Query:
            {query}
        """

        peter_agent = Agent(
            name="Peter Thiel Orchestrator",
            instructions=PETER_THIEL_PROFILE,
            tools=[],
        )

        with trace("Peter analysis"):
            result = await Runner.run(peter_agent, combined_context)

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
