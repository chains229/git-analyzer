import subprocess
import os

def get_commit_details(commit_hash: str) -> tuple[str, str]:
    """
    Retrieves the commit metadata and diff for a given commit hash.

    Args:
        commit_hash: The hash of the commit.

    Returns:
        A tuple containing the commit metadata and the diff.
    """
    try:
        # Get commit metadata
        metadata = subprocess.check_output(
            ["git", "show", "-s", "--format=%H%n%an%n%ae%n%at%n%s", commit_hash],
            encoding="utf-8"
        ).strip()

        # Get commit diff
        diff = subprocess.check_output(
            ["git", "show", "--pretty=format:", commit_hash],
            encoding="utf-8"
        ).strip()

        return metadata, diff
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Could not get details for commit {commit_hash}. Is it a valid commit hash?") from e

def save_output(output: str, output_dir: str, commit_hash: str, command: str):
    """
    Saves the output to a text file.

    Args:
        output: The string to be saved.
        output_dir: The directory to save the file in.
        commit_hash: The commit hash, used for the filename.
        command: The command that was run, used for the filename.
    """
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, f"{commit_hash}_{command}_result.txt")
    with open(file_path, "w") as f:
        f.write(output)
    print(f"Output saved to {file_path}")

def get_latest_commit_hash() -> str:
    """
    Retrieves the hash of the latest commit in the repository.

    Returns:
        The latest commit hash as a string.
    """
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            encoding="utf-8"
        ).strip()
    except subprocess.CalledProcessError as e:
        raise ValueError("Could not get the latest commit hash. It looks like you're not in a git repository?") from e