from langgraph.graph import StateGraph

def build_graph():
    graph = StateGraph(dict)

    def pricing_node(state):
        query = state.get("query", "")
        state["result"] = f"Processed query: {query}"
        return state

    graph.add_node("pricing", pricing_node)
    graph.set_entry_point("pricing")

    return graph.compile()
