# Octagon VC Agents

A MCP server that exposes AI-powered investor agent simulations augmented with Octagon Private Markets data.

![Octagon VC Agents](https://docs.octagonagents.com/octagon-vc-agents.png)

Install Octagon VC Agents for Claude Desktop in one step:
```bash
npx -y @smithery/cli@latest install @OctagonAI/investor-mcp-server --client claude
```

## Features

### Individual Investor Personas

- **Fred Wilson (Union Square Ventures)**: Simulation of the NYC-based VC known for community-driven ventures
- **Peter Thiel (Founders Fund)**: Simulation of the contrarian investor focused on disruptive technologies

### Octagon Private Markets Data Agents

- **Private Market Agents**: Provides private markets data

## Installation

### Prerequisites

- Python 3.11+
- [uv](https://github.com/octagonai/investor-mcp-server) package manager
- OpenAI API key
- Octagon API key

### Install via Smithery

```bash
npx -y @smithery/cli@latest install @OctagonAI/investor-mcp-server --client claude
```

### Claude Desktop Configuration

```json
"mcpServers": {
  "investor-persona-mcp-server": {
    "command": "uvx",
    "args": ["investor-persona-mcp-server"],
    "env": {
        "OPENAI_API_KEY": "your-openai-key-here",
        "OCTAGON_API_KEY": "your-octagon-key-here",
        "OCTAGON_BASE_URL": "https://api-gateway.octagonagents.com/v1"
    }
  }
}
```

## Implementation Details

### Persona Configuration

Investor personas are defined through markdown files containing:
- Investment philosophy
- Psychological profile
- Historical track record
- Decision-making patterns
- Communication style preferences

### Customization Options

1. Add new investor personas by creating markdown profiles
2. Implement custom interaction patterns between personas
3. Enhance orchestration logic for complex multi-perspective analysis

## Configuration

Environment variables:
- `OPENAI_API_KEY`: Required for AI model access
- `OCTAGON_API_KEY`: Required for Octagon API access  
- `OCTAGON_BASE_URL`: Base URL for Octagon API (default: "https://api-gateway.octagonagents.com/v1")
- `MCP_TRANSPORT`: Transport protocol (default: "stdio")
- `PERSONAS_DIR`: Path to investor profiles (default: "./investors")

## Development

```bash
# Clone repo
git clone https://github.com/octagonai/investor-mcp-server.git
cd investor-persona-mcp-server

# Setup environment
uv venv
source .venv/bin/activate
uv sync --dev

# Run with SSE transport
export OPENAI_API_KEY=your-openai-key
export OCTAGON_API_KEY=your-octagon-key
uv run mcp dev src/agents_mcp_server/server.py
```

Test via MCP Inspector at http://localhost:5173

## License
MIT
# investor-mcp

[![smithery badge](https://smithery.ai/badge/@octagonai/investor-mcp-server)](https://smithery.ai/server/@octagonai/investor-mcp-server)
