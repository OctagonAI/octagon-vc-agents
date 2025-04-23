from octagon_vc_agents.cli import octagon_client
from agents import Agent, WebSearchTool, OpenAIResponsesModel, ModelSettings
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

octagon_stock_data_agent = Agent(
    name="octagon-stock-data-agent",
    handoff_description="A helpful agent that can answer questions about the stock market for public companies.",
    instructions="You are a stock agent that can get stock data.",
    model=OpenAIResponsesModel(model="octagon-stock-data-agent", openai_client=octagon_client),
    tools=[],
)

octagon_sec_agent = Agent(
    name="octagon-sec-agent",
    handoff_description="A helpful agent that can answer questions about the SEC for public companies.",
    instructions="You are a SEC agent that can get SEC data.",
    model=OpenAIResponsesModel(model="octagon-sec-agent", openai_client=octagon_client),
    tools=[],
)

octagon_companies_agent = Agent(
    name="octagon-companies-agent",
    handoff_description="A helpful agent that can answer questions about the private companies in the Octagon database.",
    instructions="You are a company agent that can get company data.",
    model=OpenAIResponsesModel(model="octagon-companies-agent", openai_client=octagon_client),
    tools=[],
)


octagon_scraper_agent = Agent(
    name="octagon-scraper-agent",
    handoff_description=" A helpful agent that can scrape the website for information about a company.",
    instructions="Always return the markdown of a website URL",
    model=OpenAIResponsesModel(model="octagon-scraper-agent", openai_client=octagon_client),
    tools=[],
)


octagon_metrics_agent = Agent(
    name="octagon-metrics-agent",
    handoff_description=" A helpful assistant that can answer questions about the metrics of a company.",
    instructions="You are a metrics agent that can get metrics data for a company.",
    model=OpenAIResponsesModel(model="octagon-metrics-agent", openai_client=octagon_client),
    tools=[],
)

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
        web_search_agent.as_tool(
            tool_name="web-search-agent",
            tool_description="Always use this tool to complement your knowledge with web search data.",
        ),
        octagon_stock_data_agent.as_tool(
            tool_name="octagon-stock-data-agent",
            tool_description="Get the latest stock data for a company.",
        ),
        octagon_sec_agent.as_tool(
            tool_name="octagon-sec-agent",
            tool_description="Get the latest SEC data for a company.",
        ),
        octagon_companies_agent.as_tool(
            tool_name="octagon-companies-agent",
            tool_description="Get private company data profiles.",
            ),
        octagon_scraper_agent.as_tool(
            tool_name="octagon-scraper-agent",
            tool_description="Get the latest information about a company from the web.",
            ),
        octagon_metrics_agent.as_tool(
            tool_name="octagon-metrics-agent",
            tool_description="Get the latest financial metrics data for a publicly traded company.",
            )
        ]
    )