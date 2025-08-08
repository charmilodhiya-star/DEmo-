import streamlit as st

st.title("Project Readiness Scorer")

land = st.selectbox("Land Secured?", ["Yes", "No"])
grid = st.selectbox("Grid Secured?", ["Yes", "No"])
budget = st.number_input("Budget Spent (€)", min_value=0)
score = 0

if land == "Yes":
    score += 30
if grid == "Yes":
    score += 30
if budget > 500000:
    score += 20
score += 20  # Base

st.metric("Readiness Score", f"{score}/100")
