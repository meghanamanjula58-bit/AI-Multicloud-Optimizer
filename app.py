
import streamlit as st
import plotly.express as px

from cloud_data import get_cloud_data
from database import initialize_database

st.set_page_config(
    page_title="MultiCloud AI Manager",
    page_icon="☁️",
    layout="wide"
)

initialize_database()

data = get_cloud_data()

st.title("☁️ MultiCloud AI Manager")

st.markdown(
    "### AI-Based Multi-Cloud Resource Management and Optimization System"
)

st.write(
    "Welcome! Monitor AWS, Azure and Google Cloud resources "
    "from one dashboard."
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Cloud Providers", len(data))

c2.metric("Total Resources", len(data))

c3.metric(
    "Average CPU Usage",
    f"{data['CPU'].mean():.1f}%"
)

c4.metric(
    "Total Monthly Cost",
    f"₹{data['Cost'].sum():,}"
)

st.divider()

st.subheader("Cloud Resource Overview")

fig = px.bar(
    data,
    x="Cloud",
    y=["CPU", "Memory", "Storage"],
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Cloud Provider Information")

st.dataframe(data, use_container_width=True)

st.info(
    "Use the navigation menu to access Cloud Monitoring, "
    "Cost Analysis, AI Assistant, Optimization and Reports."
)
