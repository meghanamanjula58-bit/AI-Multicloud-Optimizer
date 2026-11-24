import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Cloud Monitoring")

st.subheader("Cloud Resource Usage")

data = pd.DataFrame({
    "Cloud Provider": ["AWS", "Azure", "Google Cloud"],
    "CPU Usage (%)": [65, 72, 55],
    "Memory Usage (%)": [70, 60, 50],
    "Storage Usage (%)": [80, 65, 45]
})

st.dataframe(data, use_container_width=True)

fig = px.bar(
    data,
    x="Cloud Provider",
    y=["CPU Usage (%)", "Memory Usage (%)", "Storage Usage (%)"],
    barmode="group",
    title="Cloud Resource Utilization"
)

st.plotly_chart(fig, use_container_width=True)
