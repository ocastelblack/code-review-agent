import typer
from rich import print
from app.agent.graph import build_graph

app = typer.Typer()
agent = build_graph()

@app.command()
def review(branch: str):
    result = agent.invoke({"branch": branch})
    print(result)
