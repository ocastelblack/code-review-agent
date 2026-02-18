from typing import TypedDict, List, Dict, Any

class ReviewState(TypedDict):
    branch: str
    modified_files: List[str]
    diffs: Dict[str, str]
    static_issues: List[Dict[str, Any]]
    llm_findings: List[Dict[str, Any]]
    question: str
    answer: str
