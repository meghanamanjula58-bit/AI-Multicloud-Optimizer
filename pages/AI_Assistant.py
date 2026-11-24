import streamlit as st

st.title("🤖 AI Assistant")

st.subheader("Cloud Optimization Assistant")

st.write(
    "Welcome to the AI Cloud Assistant. "
    "Ask questions about cloud monitoring, "
    "cloud costs and resource optimization."
)

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if question:
        st.info("AI Assistant Analysis")

        q = question.lower()

        if "cost" in q:
            st.write("Compare AWS, Azure and Google Cloud costs to identify savings.")
        elif "cpu" in q:
            st.write("Monitor CPU usage and optimize resource allocation.")
        elif "storage" in q:
            st.write("Review storage usage and remove unnecessary resources.")
        else:
            st.write("Review cloud resource utilization and optimization recommendations.")
    else:
        st.warning("Please enter a question.")
