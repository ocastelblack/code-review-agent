from git import Repo

class GitService:
    def __init__(self, repo_path="."):
        self.repo = Repo(repo_path)

    def get_modified_files(self, branch: str):
        self.repo.git.checkout(branch)
        diff_output = self.repo.git.diff("main", name_only=True)
        return diff_output.splitlines()

    def get_file_diff(self, branch: str, file_path: str):
        self.repo.git.checkout(branch)
        return self.repo.git.diff("main", file_path)
