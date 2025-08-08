import streamlit as st
from datetime import datetime

st.title("Project Scoring Tool           "
"       /---Demo in Python with a browser interface---")

# Inputs from the user
land = st.selectbox("Is land secured?", ["Yes", "No"])
grid = st.selectbox("Is grid secured?", ["Yes", "No"])
planning = st.selectbox("Is planning approved?", ["Yes", "No"])
rtb_date_str = st.date_input("Target RtB date (YYYY-MM-DD)").strftime("%Y-%m-%d")
cost_per_mw = st.number_input("Development cost per MW (€)", min_value=500000, max_value=1000000, step=10000)

# Scoring logic
def calculate_readiness(land, grid, planning, rtb_date_str, cost_per_mw):
    score = 0
    recommendation = []

    if land.lower() == 'yes':
        score += 20
    else:
        recommendation.append("Land not secured.")

    if grid.lower() == 'yes':
        score += 20
    else:
        recommendation.append("Grid not secured.")

    if planning.lower() == 'yes':
        score += 20
    else:
        recommendation.append("Planning not approved.")

    try:
        rtb_date = datetime.strptime(rtb_date_str, "%Y-%m-%d")
        if rtb_date <= datetime(2025, 6, 1):
            score += 20
        else:
            recommendation.append("RtB is later than mid-2025.")
    except:
        recommendation.append("Invalid RtB date format.")

    if cost_per_mw <= 500000:
        score += 20
    else:
        recommendation.append("High cost per MW.")

    return score, recommendation

# Run the scoring function
if st.button("Calculate Score"):
    score, recs = calculate_readiness(land, grid, planning, rtb_date_str, cost_per_mw)
    st.subheader(f"Readiness Score: {score}/100")
    
    if recs:
        st.warning(" Recommendations:")
        for rec in recs:
            st.markdown(f"- {rec}")
    else:
        st.success("Project is fully ready for next stage.")
