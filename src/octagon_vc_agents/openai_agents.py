from .client import octagon_client
from agents import Agent, WebSearchTool, OpenAIResponsesModel, ModelSettings
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")


# --- Octagon Public Market Intelligence Agents ---
octagon_sec_agent = Agent(
    name="octagon-sec-agent",
    handoff_description="A helpful agent that can answer questions about the SEC for public companies.",
    instructions="You are a SEC agent that can get SEC data.",
    model=OpenAIResponsesModel(model="octagon-sec-agent", openai_client=octagon_client),
    tools=[],
)

octagon_transcripts_agent = Agent(
    name="octagon-transcripts-agent",
    handoff_description="A helpful agent that can answer questions about the transcripts of public companies.",
    instructions="You are a transcripts agent that can get transcripts data.",
    model=OpenAIResponsesModel(model="octagon-transcripts-agent", openai_client=octagon_client),
    tools=[],
)

octagon_stock_data_agent = Agent(
    name="octagon-stock-data-agent",
    handoff_description="A helpful agent that can answer questions about the stock market for public companies.",
    instructions="You are a stock agent that can get stock data.",
    model=OpenAIResponsesModel(model="octagon-stock-data-agent", openai_client=octagon_client),
    tools=[],
)

octagon_financials_agent = Agent(
    name="octagon-financials-agent",
    handoff_description="A helpful agent that can answer questions about the financials of public companies.",
    instructions="You are a financials agent that can get financials data.",
    model=OpenAIResponsesModel(model="octagon-financials-agent", openai_client=octagon_client),
    tools=[],
)


# --- Octagon Private Company Intelligence Agents ---
octagon_companies_agent = Agent(
    name="octagon-companies-agent",
    handoff_description="A helpful agent that can answer questions about the private companies in the Octagon database.",
    instructions="You are a company agent that can get company data.",
    model=OpenAIResponsesModel(model="octagon-companies-agent", openai_client=octagon_client),
    tools=[],
)

octagon_funding_agent = Agent(
    name="octagon-funding-agent",
    handoff_description="A helpful agent that can answer questions about the funding of public companies.",
    instructions="You are a funding agent that can get funding data.",
    model=OpenAIResponsesModel(model="octagon-funding-agent", openai_client=octagon_client),
    tools=[],
)

octagon_deals_agent = Agent(
    name="octagon-deals-agent",
    handoff_description="A helpful agent that can answer questions about the deals of public companies.",
    instructions="You are a deals agent that can get deals data.",
    model=OpenAIResponsesModel(model="octagon-deals-agent", openai_client=octagon_client),
    tools=[],
)

octagon_investors_agent = Agent(
    name="octagon-investors-agent",
    handoff_description="A helpful agent that can answer questions about the investors of public companies.",
    instructions="You are a investors agent that can get investors data.",
    model=OpenAIResponsesModel(model="octagon-investors-agent", openai_client=octagon_client),
    tools=[],
)

octagon_debts_agent = Agent(
    name="octagon-debts-agent",
    handoff_description="A helpful agent that can answer questions about the debts of public companies.",
    instructions="You are a debts agent that can get debts data.",
    model=OpenAIResponsesModel(model="octagon-debts-agent", openai_client=octagon_client),
    tools=[],
)


# --- Octagon Scraper Agent ---
octagon_scraper_agent = Agent(
    name="octagon-scraper-agent",
    handoff_description=" A helpful agent that can scrape the website for information about a company.",
    instructions="Always return the markdown of a website URL",
    model=OpenAIResponsesModel(model="octagon-scraper-agent", openai_client=octagon_client),
    tools=[],
)

# --- OpenAI Web Search Agent ---
web_search_agent = Agent(
    name="web-search-agent",
    handoff_description="A helpful agent that can answer questions about the companies, such as news, articles, and social media.",
    instructions=f"""You are a web search agent that can get web search data. Focus on reliable sources, such as news articles, SEC filings, and company press releases and most recent information. Today's date is {today}.""",
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
)


def build_investor_agent(name: str, profile: dict):
    instructions = f"""
    Today's date is {today}. 
    Always use the web-search-agent to complement your knowledge. 
    If you have a website URL, use the octagon-scraper-agent to get the latest information about a company.
    If detailed financial metrics are needed, use the octagon-metrics-agent to get the latest financial metrics data for a company
    or compare to other companies that are publicly traded in the same industry.
    You are {name}, a VC with the following profile: {profile}"""
    return Agent(
        name=name,
        instructions=instructions,
        tools=[
        octagon_sec_agent.as_tool(
            tool_name="octagon-sec-agent",
            tool_description="Get the latest SEC data for a company.",
        ),
        octagon_transcripts_agent.as_tool(
            tool_name="octagon-transcripts-agent",
            tool_description="Get the latest transcripts data for a company.",
        ),
        octagon_stock_data_agent.as_tool(
            tool_name="octagon-stock-data-agent",
            tool_description="Get the latest stock data for a company.",
        ),
        octagon_financials_agent.as_tool(
            tool_name="octagon-financials-agent",
            tool_description="Get the latest financial data for a company.",
        ),  
        octagon_companies_agent.as_tool(
            tool_name="octagon-companies-agent",
            tool_description="Get private company data profiles.",
        ),
        octagon_funding_agent.as_tool(
            tool_name="octagon-funding-agent",
            tool_description="Get the latest funding data for a company.",
        ),
        octagon_deals_agent.as_tool(
            tool_name="octagon-deals-agent",
            tool_description="Get the latest deals data for a company.",
        ),
        octagon_investors_agent.as_tool(
            tool_name="octagon-investors-agent",
            tool_description="Get the latest investors data for a company.",
        ),  
        octagon_debts_agent.as_tool(
            tool_name="octagon-debts-agent",
            tool_description="Get the latest debts data for a company.",
        ),
        octagon_scraper_agent.as_tool(
            tool_name="octagon-scraper-agent",
            tool_description="Get the latest information about a company from the web.",
        ),
        web_search_agent.as_tool(
            tool_name="web-search-agent",
            tool_description="Always use this tool to complement your knowledge with web search data.",
        )
        ],
        model="gpt-4.1"
    )