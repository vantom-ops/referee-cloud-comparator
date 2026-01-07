import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from comparator import compare_services
from utils import export_pdf  # We'll update export_pdf to return bytes

st.set_page_config(page_title="Cloud Referee", layout="wide")

st.title("🧠 Cloud Referee – Decision Assistant")
st.caption("Compare cloud services with scores and trade-offs")

# --- User Inputs ---
traffic = st.selectbox("Traffic Pattern", ["Low", "Spiky", "High"])
budget = st.selectbox("Budget Priority", ["Low", "Medium", "High"])
ops = st.selectbox("DevOps Experience", ["Low", "Medium", "High"])

# --- Compare Services ---
if st.button("Compare Services"):
    results = compare_services(traffic, budget, ops)

    # Convert results to DataFrame
    df = pd.DataFrame([
        {
            "Service": name,
            "Score": data["score"],
            "Pros": ", ".join(data["pros"]),
            "Cons": ", ".join(data["cons"])
        }
        for name, data in results.items()
    ])

    # --- Side-by-Side Table ---
    st.subheader("📋 Side-by-Side Comparison")
    st.dataframe(df, use_container_width=True)

    # --- Score Bar Visualization ---
    st.subheader("📊 Score Visualization")
    fig, ax = plt.subplots()
    ax.bar(df["Service"], df["Score"], color='skyblue')
    ax.set_ylabel("Decision Score")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

    # --- Recommended Choice ---
    winner = df.sort_values("Score", ascending=False).iloc[0]
    st.success(f"✅ Recommended Choice: **{winner['Service']}**")

    # --- PDF Export & Download ---
    # Create a unique download button
    pdf_bytes = export_pdf(df, winner)  # Make sure this returns bytes (see below)
    st.download_button(
        label="📄 Download Decision Report as PDF",
        data=pdf_bytes,
        file_name="decision_report.pdf",
        mime="application/pdf"
    )
