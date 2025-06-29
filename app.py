import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Fraud Strategy Builder", layout="centered")
st.title("🛡️ Retail Fraud Strategy Builder")

# Section 1: Business Goals
st.header("1. Select Your Business Goals")
business_goals = ["Efficiency", "Growth", "Customer Experience", "Risk Management", "Innovation"]
selected_goals = st.multiselect("Choose business goals:", business_goals)

# Section 2: Use Cases
use_case_map = {
    "Efficiency": ["Reporting", "Process Analytics"],
    "Growth": ["Customer Segmentation", "Predictive Models", "Cross-sell Analytics"],
    "Customer Experience": ["Real-time Monitoring", "Personalization", "Generative AI"],
    "Risk Management": ["Fraud Detection", "Compliance Analytics"],
    "Innovation": ["Generative AI", "Optimization Models"]
}
st.header("2. Choose Your Use Cases")
selected_use_cases = []
for goal in selected_goals:
    st.markdown(f"**{goal} Use Cases**")
    selected = st.multiselect(f"Select for {goal}", use_case_map.get(goal, []), key=goal)
    selected_use_cases.extend(selected)

# Section 3: Risk Matrix
st.header("3. Identify Fraud Risk vs Business Impact")
risk_level = st.selectbox("Fraud Risk Level", ["Low", "High"])
impact_level = st.selectbox("Business Impact", ["Low", "High"])

quadrant_map = {
    ("Low", "Low"): "🟢 Routine Monitoring",
    ("High", "Low"): "⚫ Process Surveillance",
    ("Low", "High"): "🟠 Strategic Control",
    ("High", "High"): "🔴 Critical Watchlist"
}
quadrant = quadrant_map[(risk_level, impact_level)]
st.success(f"Your risk quadrant is: {quadrant}")

# Plot matrix
fig, ax = plt.subplots()
ax.set_title("Fraud Risk vs Business Impact")
ax.set_xlabel("Business Impact")
ax.set_ylabel("Fraud Risk Level")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Low", "High"])
ax.set_yticklabels(["Low", "High"])
ax.grid(True)
colors = {
    ("Low", "Low"): "green",
    ("High", "Low"): "black",
    ("Low", "High"): "orange",
    ("High", "High"): "red"
}
pos = {
    ("Low", "Low"): (0.25, 0.25),
    ("High", "Low"): (0.25, 0.75),
    ("Low", "High"): (0.75, 0.25),
    ("High", "High"): (0.75, 0.75)
}
x, y = pos[(risk_level, impact_level)]
ax.scatter(x, y, color=colors[(risk_level, impact_level)], s=300)
st.pyplot(fig)

# Section 4: Framework Summary
if st.button("🚀 Generate Your Data Strategy"):
    st.subheader("🎯 Your Personalized Data Strategy")
    st.write("**Business Goals:**", ", ".join(selected_goals))
    st.write("**Use Cases:**", ", ".join(selected_use_cases))
    st.write("**Risk Quadrant:**", quadrant)
    st.write("**Architecture:** Lakehouse + Stream Processing")
    st.write("**Data Requirements:** Event Stream, Streaming Processing")
    st.write("**Governance:** Moderate Governance")

    with st.expander("🧠 Full Framework & Playbook Summary"):
        st.markdown(open("framework.md", encoding="utf-8").read())
