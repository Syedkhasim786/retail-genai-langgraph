
from graph.retail_graph import build_graph

app = FastAPI()
graph = build_graph()

@app.get("/")
def home():
    return {"message": "Retail GenAI API running"}

@app.get("/ask")
def ask(query: str):
    result = graph.invoke({"query": query})
    return result
