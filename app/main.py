import streamlit as st
from graph.retail_graph import build_graph

st.title("🛒 Retail GenAI Assistant")

query = st.text_input("Ask your retail question:")

if st.button("Submit"):
    graph = build_graph()
    result = graph.invoke({"query": query})
    st.write(result["result"])
