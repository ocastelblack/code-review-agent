from git import Repo

class GitService:
    def __init__(self, repo_path="."):
        self.repo = Repo(repo_path)

    def get_file_content(self, branch: str, file_path: str):
        return self.repo.git.show(f"{branch}:{file_path}")

    def get_modified_files(self, branch: str):
        diff_output = self.repo.git.diff(f"main..{branch}", "--", name_only=True)
        return diff_output.splitlines()


    def get_file_diff(self, branch: str, file_path: str):
        return self.repo.git.diff(f"main..{branch}", "--", file_path)
