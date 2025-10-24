from crewai import Agent
from source.prompts.prompt_agents import REVIEW_PROMPT
from source.tools.get_file_content import GetFileContentTool
from source.tools.search_risk_info import SearchRiskInfoTool

def create_review_agent(llm):
    return Agent(
        role="Senior Software Engineer",
        goal="Review uncommitted changes in a git repository for code quality, logical bugs, security, and style issues.",
        backstory=(
            "You are an experienced software engineer with a strong background in code reviews. "
            "You excel at identifying potential issues and providing constructive feedback to improve code quality."
        ),
        prompt=REVIEW_PROMPT,
        llm=llm,
        tools=[GetFileContentTool(), SearchRiskInfoTool()],
        verbose=False,
    )