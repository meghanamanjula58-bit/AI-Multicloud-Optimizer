import streamlit as st
import pandas as pd
import plotly.express as px

st.title("☁️ MultiCloud AI Manager")

st.subheader("Cloud Dashboard")

data = pd.DataFrame({
    "Cloud": ["AWS", "Azure", "Google Cloud"],
    "Cost": [4500, 3500, 2800],
    "Usage": [75, 65, 55]
})

st.dataframe(data, use_container_width=True)

fig = px.bar(data, x="Cloud", y="Cost",
             title="Cloud Cost Comparison")

st.plotly_chart(fig, use_container_width=True)
