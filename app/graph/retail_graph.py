from langgraph.graph import StateGraph
from graph.tools.pricing_tool import optimize_price

def build_graph():
    graph = StateGraph(dict)

    def pricing_node(state):
        query = state.get("query", "").lower()

        # Extract values from query with defaults
        cost = 100
        competitor_price = 120
        demand = "high"
        stock = "low"

        if "cost is" in query:
            try:
                cost = float(query.split("cost is")[1].split(",")[0].strip())
            except:
                pass

        if "competitor price is" in query:
            try:
                competitor_price = float(query.split("competitor price is")[1].split(",")[0].strip())
            except:
                pass

        if "demand is" in query:
            demand = "high" if "high" in query.split("demand is")[1].split(",")[0] else "low"

        if "stock is" in query:
            stock = "low" if "low" in query.split("stock is")[1].split(",")[0] else "high"

        price = optimize_price(cost, competitor_price, demand, stock)
        state["result"] = f"Recommended price: ${price}"
        return state

    graph.add_node("pricing", pricing_node)
    graph.set_entry_point("pricing")
    return graph.compile()
