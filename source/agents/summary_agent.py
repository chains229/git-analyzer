from crewai import Agent
from source.prompts.prompt_agents import SUMMARY_PROMPT
from source.tools.get_file_content import GetFileContentTool
from source.tools.search_risk_info import SearchRiskInfoTool

def create_summary_agent(llm):
    return Agent(
        role="Code Change Summarizer",
        goal="Provide a concise and clear summary of the changes in a git commit.",
        backstory=(
            "You are an experienced software engineer with a knack for "
            "explaining complex code changes in a simple and understandable way."
        ),
        prompt=SUMMARY_PROMPT,
        llm=llm,
        tools=[GetFileContentTool(), SearchRiskInfoTool()],
        verbose=True,
    )