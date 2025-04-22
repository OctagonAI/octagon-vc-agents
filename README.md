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

## MCP Client Installation Instructions

#### Running on Claude Desktop
To configure Octagon MCP for Claude Desktop:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client claude
```

#### Running on Cursor
To configure Octagon MCP in Cursor:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client cursor
```

#### Running on VSCode
To configure Octagon MCP for VSCode:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client vscode
```

#### Running on VSCode Insiders
To configure Octagon MCP for VSCode Insiders:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client vscode-insiders
```

#### Running on Windsurf
To configure Octagon MCP for Windsurf:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client windsurf
```

#### Running on Roocode
To configure Octagon MCP for Roocode:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client roocode
```

#### Running on Witsy
To configure Octagon MCP for Witsy:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client witsy
```

#### Running on Enconvo
To configure Octagon MCP for Enconvo:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client enconvo
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


## License
MIT


[![smithery badge](https://smithery.ai/badge/@octagonai/investor-mcp-server)](https://smithery.ai/server/@octagonai/investor-mcp-server)
