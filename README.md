# Octagon VC Agents

A MCP server that exposes AI-powered investor agent simulations augmented with Octagon Private Markets data.

![Octagon VC Agents](https://docs.octagonagents.com/octagon-vc-agents.png)

Install Octagon VC Agents for Claude Desktop in one step:
```bash
npx -y @smithery/cli@latest install @OctagonAI/investor-mcp-server --client claude
```

## Octagon VC Agents

These are AI-powered simulations inspired by notable venture capitalists. These personas are not affiliated with or endorsed by the actual individuals.

| VC Agent Name | Description |
|------------|-------------|
| `octagon-marc-andreessen-agent` | Simulation of the tech-optimist investor known for "software eating the world" thesis and bold technology bets |
| `octagon-peter-thiel-agent` | Simulation of the venture capitalist & 'Zero to One' author who analyzes investments through the lens of monopoly theory and contrarian thinking |
| `octagon-reid-hoffman-agent` | Simulation of the LinkedIn founder-turned-investor known for network-effect businesses and blitzscaling philosophy |
| `octagon-keith-rabois-agent` | Simulation of the operator-investor known for spotting exceptional talent and operational excellence |
| `octagon-bill-gurley-agent` | Simulation of the analytical investor known for marketplace expertise and detailed market analysis |
| `octagon-fred-wilson-agent` | Simulation of the USV co-founder & veteran early-stage investor focused on community-driven networks and founder-first philosophies |
| `octagon-josh-kopelman-agent` | Simulation of the founder-friendly investor focused on seed-stage companies and founder development |
| `octagon-alfred-lin-agent` | Simulation of the operator-turned-investor known for consumer businesses and organizational scaling |

## MCP Client Installation Instructions

#### Running on Claude Desktop
To configure Octagon VC Agents for Claude Desktop:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client claude
```

#### Running on Cursor
To configure Octagon VC Agents in Cursor:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client cursor
```

#### Running on VSCode
To configure Octagon VC Agents for VSCode:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client vscode
```

#### Running on VSCode Insiders
To configure Octagon VC Agents for VSCode Insiders:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client vscode-insiders
```

#### Running on Windsurf
To configure Octagon VC Agents for Windsurf:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client windsurf
```

#### Running on Roocode
To configure Octagon VC Agents for Roocode:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client roocode
```

#### Running on Witsy
To configure Octagon VC Agents for Witsy:

```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client witsy
```

#### Running on Enconvo
To configure Octagon VC Agents for Enconvo:

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

## License
MIT

[![smithery badge](https://smithery.ai/badge/@octagonai/investor-mcp-server)](https://smithery.ai/server/@octagonai/investor-mcp-server)
