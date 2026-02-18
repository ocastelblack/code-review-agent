from app.services.git_service import GitService
import sys

if __name__ == "__main__":
    branch = sys.argv[1]
    git_service = GitService()

    files = git_service.get_modified_files(branch)

    print("Archivos modificados:")
    for f in files:
        print("-", f)
