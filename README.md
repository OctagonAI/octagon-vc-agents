# Octagon VC Agents

A MCP server that exposes AI-powered investor agent simulations augmented with Octagon Private Markets data.

![Octagon VC Agents](https://docs.octagonagents.com/octagon-vc-agents.png)

Install Octagon VC Agents for Claude Desktop in one step:
```bash
npx -y @smithery/cli@latest install @OctagonAI/octagon-vc-agents --client claude
```

## Octagon VC Agents

These are AI-powered simulations inspired by notable venture capitalists. These personas are not affiliated with or endorsed by the actual individuals.

| VC Agent Name | Description |
|------------|-------------|
| [`octagon-marc-andreessen-agent`](src/octagon_vc_agents/investors/marc_andreessen.md) | Simulation of the tech-optimist investor known for "software eating the world" thesis and bold technology bets |
| [`octagon-peter-thiel-agent`](src/octagon_vc_agents/investors/peter_thiel.md) | Simulation of the venture capitalist & 'Zero to One' author who analyzes investments through the lens of monopoly theory and contrarian thinking |
| [`octagon-reid-hoffman-agent`](src/octagon_vc_agents/investors/reid_hoffman.md) | Simulation of the LinkedIn founder-turned-investor known for network-effect businesses and blitzscaling philosophy |
| [`octagon-keith-rabois-agent`](src/octagon_vc_agents/investors/keith_rabois.md) | Simulation of the operator-investor known for spotting exceptional talent and operational excellence |
| [`octagon-bill-gurley-agent`](src/octagon_vc_agents/investors/bill_gurley.md) | Simulation of the analytical investor known for marketplace expertise and detailed market analysis |
| [`octagon-fred-wilson-agent`](src/octagon_vc_agents/investors/fred_wilson.md) | Simulation of the USV co-founder & veteran early-stage investor focused on community-driven networks and founder-first philosophies |
| [`octagon-josh-kopelman-agent`](src/octagon_vc_agents/investors/josh_kopelman.md) | Simulation of the founder-friendly investor focused on seed-stage companies and founder development |
| [`octagon-alfred-lin-agent`](src/octagon_vc_agents/investors/alfred_lin.md) | Simulation of the operator-turned-investor known for consumer businesses and organizational scaling |

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

## Documentation

For detailed information about Octagon Agents, including setup guides, API reference, and best practices, visit our [documentation](https://docs.octagonagents.com).

## License
MIT

[![smithery badge](https://smithery.ai/badge/@octagonai/octagon-vc-agents)](https://smithery.ai/server/@octagonai/octagon-vc-agents)
