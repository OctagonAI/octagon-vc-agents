from pathlib import Path
from mcp.server.fastmcp import FastMCP

from octagon_vc_agents.agent_registrar import AgentRegistrar
from octagon_vc_agents.vc_agents import OCTAGON_VC_AGENTS
from octagon_vc_agents.openai_agents import build_investor_agent


# --- Helper to load investor profiles ---
def load_profile(slug: str) -> str:
    return (Path(__file__).parent / f"investors/{slug}.md").read_text()


# --- FastMCP server setup ---
mcp = FastMCP(
    name="Octagon VC Agents",
    instructions="Access investor agents through the Model Context Protocol."
)

# --- Initialize agent registrar ---
registrar = AgentRegistrar(mcp)


# --- Register Investor Agents from Config ---
for name, slug, description in OCTAGON_VC_AGENTS:
    registrar.register(
        name=name,
        description=description,
        build_agent=lambda n=name, s=slug: build_investor_agent(n, load_profile(s)),
        vc_agent=True,
        has_field_description=True,
        octagon_activated=True
    )
