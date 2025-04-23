# Octagon VC Agents

[![smithery badge](https://smithery.ai/badge/@OctagonAI/octagon-vc-agents)](https://smithery.ai/server/@OctagonAI/octagon-vc-agents)

An MCP server that runs AI-driven venture capitalist agents (Fred Wilson, Peter Thiel, etc.), whose thinking is continuously enriched by Octagon Private Markets' real-time deals, valuations, and deep research intelligence. Use it to spin up programmable "VC brains" for pitch feedback, diligence simulations, term sheet negotiations, and more.

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

## Example Prompts

| What you want from the agents | Copy-and-paste prompt |
|-------------------------------|-----------------------|
| Deal critique                 | Ask `@octagon-marc-andreessen-agent` and `@octagon-reid-hoffman-agent` to evaluate {company website}'s latest funding round. Provide a detailed comparative table from their points of view. |
| Qualify investor fit before the call | `@octagon-alfred-lin-agent` You're vetting my pre-seed startup: {one-sentence pitch}. In {deck.pdf}, you'll find our vision, team, and WAU chart. Give me a "meet/pass" decision and list the three metrics I should strengthen most before your partner vote on Monday. |
| Thesis & metrics reality-check | `@octagon-reid-hoffman-agent` Here's our 10-slide deck and dashboard ({docs}). We currently have {X} weekly active users, {Y}% MoM WAU growth, and {Z}% retention over 8 weeks. Using your 14-day diligence lens, list the biggest metric gaps that would prevent you from issuing a term sheet, and suggest how we could close them within one quarter. |
| Portfolio-intro mapping – warm leads for the next round | `@octagon-fred-wilson-agent` Based on your current portfolio in {data} and our focus (outlined in the one-pager below), identify four portfolio CEOs who could become design partners. For each CEO, draft a first-contact email from me that highlights mutual value. |

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

