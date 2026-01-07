import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from comparator import compare_services
from utils import export_pdf

st.set_page_config(page_title="Cloud Referee", layout="wide")

st.title("🧠 Cloud Referee – Decision Assistant")
st.caption("Compare cloud services with scores and trade-offs")

traffic = st.selectbox("Traffic Pattern", ["Low", "Spiky", "High"])
budget = st.selectbox("Budget Priority", ["Low", "Medium", "High"])
ops = st.selectbox("DevOps Experience", ["Low", "Medium", "High"])

if st.button("Compare Services"):
    results = compare_services(traffic, budget, ops)

    df = pd.DataFrame([
        {
            "Service": name,
            "Score": data["score"],
            "Pros": ", ".join(data["pros"]),
            "Cons": ", ".join(data["cons"])
        }
        for name, data in results.items()
    ])

    st.subheader("📋 Side-by-Side Comparison")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Score Visualization")
    fig, ax = plt.subplots()
    ax.bar(df["Service"], df["Score"])
    ax.set_ylabel("Decision Score")
    st.pyplot(fig)

    winner = df.sort_values("Score", ascending=False).iloc[0]
    st.success(f"✅ Recommended Choice: **{winner['Service']}**")

    if st.button("📄 Export Decision as PDF"):
        export_pdf(df, winner)
        st.success("PDF exported as decision_report.pdf")
