import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚙️ Cloud Optimization")

st.subheader("AI-Based Resource Optimization")

data = pd.DataFrame({
    "Cloud": ["AWS", "Azure", "Google Cloud"],
    "CPU Usage": [85, 45, 70],
    "Monthly Cost": [4500, 3500, 2800]
})

st.dataframe(data, use_container_width=True)

st.subheader("Optimization Recommendations")

for _, row in data.iterrows():
    if row["CPU Usage"] > 80:
        st.warning(f'{row["Cloud"]}: High CPU usage. Review resource allocation.')
    elif row["CPU Usage"] < 50:
        st.info(f'{row["Cloud"]}: Low CPU usage. Consider optimizing resources.')
    else:
        st.success(f'{row["Cloud"]}: Resource usage is within the selected range.')

st.subheader("CPU Usage Comparison")

fig = px.bar(
    data,
    x="Cloud",
    y="CPU Usage",
    title="Cloud CPU Utilization",
    text="CPU Usage"
)

st.plotly_chart(fig, use_container_width=True)
