import subprocess
from crewai.tools import BaseTool
from source.prompts.prompt_tool import GET_FILE_CONTENT_PROMPT

class GetFileContentTool(BaseTool):
    name: str = "Get File Content"
    description: str = GET_FILE_CONTENT_PROMPT

    def _run(self, file_path: str, commit_hash: str) -> str:
        """
        Gets the content of a file at a specific commit.

        Args:
            file_path: The path to the file.
            commit_hash: The commit hash to get the file content from.

        Returns:
            The content of the file as a string.
        """
        try:
            return subprocess.check_output(
                ["git", "show", f"{commit_hash}:{file_path}"],
                encoding="utf-8"
            ).strip()
        except subprocess.CalledProcessError:
            return f"Error: Could not retrieve content of file '{file_path}' at commit '{commit_hash}'."