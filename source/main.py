import argparse
from dotenv import load_dotenv
from crewai import Crew, Task

from source.agents.summary_agent import create_summary_agent
from source.agents.analyze_agent import create_analyze_agent
from source.utils import get_commit_details, save_output

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Analyzes git commits using AI agents.")
    parser.add_argument(
        "main_command",
        choices=["summary", "analyze"],
        help="The main command to run (summary or analyze). Defaults to summary."
    )
    parser.add_argument("--commit", required=True, help="The git commit hash to analyze.")
    parser.add_argument(
        "--model",
        default="azure/gpt-4.1",
        help="The LLM model to use. Defaults to gpt-4.1"
    )
    parser.add_argument(
        "--output-dir",
        help="The directory to save the output file. If not provided, output is printed to the terminal."
    )

    args = parser.parse_args()

    try:
        metadata, diff = get_commit_details(args.commit)
    except ValueError as e:
        print(e)
        return

    llm = args.model

    if args.main_command == "summary":
        agent = create_summary_agent(llm)
        task = Task(
            description=f"Summarize the following git commit:\n\nMetadata:\n{metadata}\n\nDiff:\n{diff}",
            agent=agent,
            expected_output="A concise summary of the git commit."
        )
    elif args.main_command == "analyze":
        agent = create_analyze_agent(llm)
        task = Task(
            description=f"Analyze the following git commit for security and performance risks:\n\nMetadata:\n{metadata}\n\nDiff:\n{diff}",
            agent=agent,
            expected_output="A detailed analysis of security and performance risks, if any, with mitigation suggestions."
        )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )

    result = crew.kickoff()

    print("\n" + "="*50)
    print("      Git Commit Analysis Result")
    print("="*50 + "\n")
    print(result)

    if args.output_dir:
        save_output(result, args.output_dir, args.commit, args.main_command)

if __name__ == "__main__":
    main()