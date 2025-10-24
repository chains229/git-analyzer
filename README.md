# Git Analyzer

A simple command-line interface (CLI) tool that leverages AI agents to analyze Git commits for potential security and performance risks.

## Features

- **Commit Summarization**: Provides a concise summary of the changes in a given commit.
- **Risk Analysis**: Identifies potential security vulnerabilities and performance bottlenecks introduced in a commit.
- **Code Review**: Summaries and identifies potential vulnerabilities in repo diff before committing.
- **Extensible LLM Support**: Easily configure different Language Model (LLM) providers through CrewAI.
- **File Content Retrieval**: Agents can fetch the full content of a file for more in-depth analysis.
- **External Information Search**: Agents can search for information about identified risks and provide relevant links.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chains229/git-analyzer.git
    cd git-analyzer
    ```

2.  **Install dependencies using uv:**
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    -   Create a `.env` file from the `.env.example`:
        ```bash
        cp .env.example .env
        ```
    -   Open the `.env` file and add your Azure OpenAI API key.
    -   You can custom the default model in `source/main.py` and the API key to use your preferred model.

## Usage

First, enter the virtual environment of this repo

```shell
-m venv .venv
source .venv/bin/activate  # On Linux/macOS
.\.venv\Scripts\activate   # On Windows
```
Then, `cd` to the repo that contains the commit you want to analyze (i know it sucks). 
The main command to run the analyzer is `ga`.

- To summary a commit:

```shell
ga summary --commit <your-commit-id>
```

- To analyze performance/security risk of a commit:
```shell
ga summary --commit <your-commit-id>
```

- To review uncommitted code:
```shell
ga review
```

### Optional argument

- `--model`: Choose the LLM you want.
- `--output-dir`: You can save the result into a .txt file by setting this argument. (dont think it's working)