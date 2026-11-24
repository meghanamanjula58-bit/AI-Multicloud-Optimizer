
import streamlit as st

st.set_page_config(
    page_title="MultiCloud AI Manager",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = {
    "Main": [
        st.Page(
            "pages/Dashboard.py",
            title="Dashboard",
            icon="🏠",
            default=True
        )
    ],
    "Cloud Management": [
        st.Page("pages/Cloud_Monitoring.py", title="Cloud Monitoring", icon="📊"),
        st.Page("pages/Cost_Analysis.py", title="Cost Analysis", icon="💰"),
        st.Page("pages/AI_Assistant.py", title="AI Assistant", icon="🤖"),
        st.Page("pages/Optimization.py", title="Optimization", icon="⚙️"),
        st.Page("pages/Reports.py", title="Reports", icon="📄")
    ]
}

navigation = st.navigation(pages, position="sidebar")
navigation.run()
