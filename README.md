# Octagon VC Agents

[![smithery badge](https://smithery.ai/badge/@OctagonAI/octagon-vc-agents)](https://smithery.ai/server/@OctagonAI/octagon-vc-agents)

An MCP server that runs AI-driven venture capitalist agents (Fred Wilson, Peter Thiel, etc.), whose thinking is continuously enriched by Octagon Private Markets' real-time deals, valuations, and deep research intelligence. Use it to spin up programmable "VC brains" for pitch feedback, diligence simulations, term sheet negotiations, and more.

<!-- Display at 60% wide and keep the aspect ratio -->
<img src="https://docs.octagonagents.com/octagon-vc-agents.png"
     alt="Octagon VC Agents"
     width="60%" />
    
## Try Demo in ChatGPT
VC Agents are also fully integrated them in ChatGPT with a demo Octagon API key. Give them a try here:
<a href="https://chatgpt.com/g/g-680c1eddd1448191bb4ed7e09485270f-vc-agents" target="_blank" rel="noopener noreferrer">VC Agents GPT</a>


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

## Prerequisites

To use Octagon VC Agents, you will need **two API keys**:
- An **Octagon API key** (for access to Octagon Private Markets data)
- An **OpenAI API key** (for AI-powered analysis)

### Get Your Octagon API Key

To use VC Agents, you need to:

1. Sign up for a free account at [Octagon](https://app.octagonai.co/signup/?redirectToAfterSignup=https://app.octagonai.co/api-keys)
2. After logging in, from left menu, navigate to **API Keys**
3. Generate a new API key
4. Use this API key in your configuration as the `OCTAGON_API_KEY` value

### Get Your OpenAI API Key

You also need an OpenAI API key to enable AI-powered features:

1. Sign up or log in at [OpenAI](https://platform.openai.com/signup)
2. Go to [API Keys](https://platform.openai.com/api-keys)
3. Create a new API key
4. Use this API key in your configuration as the `OPENAI_API_KEY` value

### Install pipx

To use Octagon VC Agents, you need [pipx](https://pypa.github.io/pipx/), a tool for installing and running Python applications in isolated environments.

#### On macOS
Install pipx using Homebrew (recommended):
```bash
brew install pipx
pipx ensurepath
```
Or with pip:
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

#### On Windows
Install pipx using pip:
```powershell
python -m pip install --user pipx
python -m pipx ensurepath
```
After installation, restart your terminal so that the `pipx` command is available.


## Installation

### Running on Claude Desktop

To configure Octagon VC Agents for Claude Desktop:

1. Open Claude Desktop
2. Go to Settings > Developer > Edit Config
3. Add the following to your `claude_desktop_config.json` (Replace `YOUR_OCTAGON_API_KEY_HERE` with your Octagon API key and `YOUR_OPENAI_API_KEY_HERE` with your OpenAI API key):
```json
{
  "mcpServers": {
    "octagon-vc-agents": {
      "command": "pipx",
      "args": ["run", "--pip-args=\"--no-cache-dir\"", "octagon-vc-agents", "run"],
      "env": {
        "OPENAI_API_KEY": "YOUR_OPENAI_API_KEY_HERE",
        "OCTAGON_API_KEY": "YOUR_OCTAGON_API_KEY_HERE"
      }
    }
  }
}
```
4. Restart Claude for the changes to take effect



### Running on Cursor

Configuring Cursor Desktop 🖥️
Note: Requires Cursor version 0.45.6+

To configure Octagon VC Agents in Cursor:

1. Open Cursor Settings
2. Go to Features > MCP Servers 
3. Click "+ Add New MCP Server"
4. Enter the following:
   - Name: "octagon-mcp" (or your preferred name)
   - Type: "command"
   - Command: `env OCTAGON_API_KEY=YOUR_OCTAGON_API_KEY_HERE OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE pipx run --pip-args="--no-cache-dir" octagon-vc-agents run`

> If you are using Windows and are running into issues, try `cmd /c "set OCTAGON_API_KEY=YOUR_OCTAGON_API_KEY_HERE && set OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE && pipx run --pip-args='--no-cache-dir' octagon-vc-agents run"`

Replace `YOUR_OCTAGON_API_KEY_HERE` with your Octagon API key and `YOUR_OPENAI_API_KEY_HERE` with your OpenAI API key.

After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use VC Agents when appropriate, but you can explicitly request it by describing your investment research needs. Access the Composer via Command+L (Mac), select "Agent" next to the submit button, and enter your query.


### Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

```json
{
  "mcpServers": {
    "octagon-vc-agents": {
      "command": "pipx",
      "args": ["run", "--pip-args=\"--no-cache-dir\"", "octagon-vc-agents", "run"],
      "env": {
        "OPENAI_API_KEY": "YOUR_OPENAI_API_KEY_HERE",
        "OCTAGON_API_KEY": "YOUR_OCTAGON_API_KEY_HERE"
      }
    }
  }
}
```

### Running with pipx

```bash
env OCTAGON_API_KEY=YOUR_OCTAGON_API_KEY_HERE OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE pipx run --pip-args="--no-cache-dir" octagon-vc-agents run
```

### Manual Installation

```bash
pip install octagon-vc-agents
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

