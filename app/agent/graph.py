from langgraph.graph import StateGraph, END
from app.agent.state import ReviewState
from app.agent.nodes import detect_changes, static_analysis, llm_review

def build_graph():
    graph = StateGraph(ReviewState)

    graph.add_node("detect_changes", detect_changes)
    graph.add_node("static_analysis", static_analysis)
    graph.add_node("llm_review", llm_review)

    graph.set_entry_point("detect_changes")
    graph.add_edge("detect_changes", "static_analysis")
    graph.add_edge("static_analysis", "llm_review")
    graph.add_edge("llm_review", END)

    return graph.compile()
