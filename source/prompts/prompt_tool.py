GET_FILE_CONTENT_PROMPT = """
You are analyzing a code change and need more context than the diff provides.
To get the full content of a file at the state of the commit, you can use the 'Get File Content' tool.
Provide the file path and the commit hash to the tool.
"""

SEARCH_RISK_INFO_PROMPT = """
You have identified a potential security or performance risk and want to provide more information to the user.
Use the 'Search for Risk Information' tool to find relevant articles, documentation, or advisories.
Provide a clear description of the risk you want to search for.
"""