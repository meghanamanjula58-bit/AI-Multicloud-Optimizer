import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📄 Cloud Reports")

st.subheader("Cloud Resource Summary")

data = pd.DataFrame({
    "Cloud Provider": ["AWS", "Azure", "Google Cloud"],
    "CPU Usage (%)": [65, 72, 55],
    "Monthly Cost (₹)": [4500, 3500, 2800],
    "Status": ["Active", "Active", "Active"]
})

st.dataframe(data, use_container_width=True)

st.subheader("Generate Cloud Report")

if st.button("Generate Report"):
    report = f"""
MULTICLOUD AI MANAGER
Cloud Resource Report

Generated: {datetime.now()}

{data.to_string(index=False)}

Total Monthly Cost: ₹{data['Monthly Cost (₹)'].sum()}
Average CPU Usage: {data['CPU Usage (%)'].mean():.2f}%
"""

    st.download_button(
        "⬇️ Download Report",
        data=report,
        file_name="Cloud_Report.txt",
        mime="text/plain"
    )

    st.success("Report generated successfully!")
