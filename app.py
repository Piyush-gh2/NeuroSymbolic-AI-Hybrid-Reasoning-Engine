import streamlit as st
from src.ml_model import train_model
from src.reasoning_engine import make_decision
from src.rag import load_knowledge, build_index, retrieve

# Train model once
train_model()

st.title("🧠 NeuroSymbolic AI Decision Engine")

marketing = st.slider("Marketing Spend", 10000, 50000, 20000)
operations = st.slider("Operations Cost", 5000, 20000, 8000)
current_revenue = st.number_input("Current Revenue", value=25000)

query = st.text_input("Ask Business Question")

if st.button("Run Simulation"):
    
    predicted, growth, decision = make_decision(
        marketing, operations, current_revenue
    )
    
    st.subheader("📊 Results")
    st.write(f"Predicted Revenue: {predicted:.2f}")
    st.write(f"Growth: {growth:.2f}%")
    st.write(f"Decision: {decision}")
    
    # RAG
    docs = load_knowledge()
    index, _ = build_index(docs)
    
    if query:
        results = retrieve(query, docs, index)
        
        st.subheader("🔎 Retrieved Insights")
        for r in results:
            st.write(r)