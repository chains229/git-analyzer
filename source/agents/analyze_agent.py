from crewai import Agent
from source.prompts.prompt_agents import ANALYSIS_PROMPT
from source.tools.get_file_content import GetFileContentTool
from source.tools.search_risk_info import SearchRiskInfoTool

def create_analyze_agent(llm):
    return Agent(
        role="Security and Performance Analyst",
        goal="Identify potential security vulnerabilities and performance issues in a git commit.",
        backstory=(
            "You are a seasoned expert in application security and performance tuning. "
            "You have a keen eye for spotting subtle issues in code that could lead to major problems."
        ),
        prompt=ANALYSIS_PROMPT,
        llm=llm,
        tools=[GetFileContentTool(), SearchRiskInfoTool()],
        verbose=False,
    )