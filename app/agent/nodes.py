from app.services.git_service import GitService
from app.services.analysis_service import AnalysisService
from app.services.llm_service import LLMService

def detect_changes(state):
    git = GitService()

    branch = state["branch"]
    files = git.get_modified_files(branch)

    diffs = {}
    for file in files:
        diffs[file] = git.get_file_diff(branch, file)

    return {
        **state,
        "modified_files": files,
        "diffs": diffs
    }

def static_analysis(state):
    analyzer = AnalysisService()
    issues = []

    git = GitService()
    branch = state["branch"]

    for file in state["modified_files"]:
        try:
            code = git.get_file_content(branch, file)
            issues.extend(analyzer.analyze_complexity(code))
        except Exception:
            continue

def llm_review(state):
    llm = LLMService()
    findings = llm.review(state["diffs"])

    return {**state, "llm_findings": findings}
