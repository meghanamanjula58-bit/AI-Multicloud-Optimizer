import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Cost Analysis")

st.subheader("Cloud Provider Cost Comparison")

data = pd.DataFrame({
    "Cloud Provider": ["AWS", "Azure", "Google Cloud"],
    "Monthly Cost": [4500, 3500, 2800]
})

col1, col2, col3 = st.columns(3)

col1.metric("AWS Cost", "₹4,500")
col2.metric("Azure Cost", "₹3,500")
col3.metric("Google Cloud Cost", "₹2,800")

st.subheader("Monthly Cloud Expenses")

st.dataframe(data, use_container_width=True)

fig = px.pie(
    data,
    names="Cloud Provider",
    values="Monthly Cost",
    title="Cloud Cost Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Cost analysis completed successfully!")
