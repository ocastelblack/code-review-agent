from fastapi import FastAPI
from app.agent.graph import build_graph

app = FastAPI()
agent = build_graph()

@app.post("/review/{branch}")
def review(branch: str):
    result = agent.invoke({"branch": branch})
    return result
