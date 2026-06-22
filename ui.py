import streamlit as st
from parser import detect_issue
from analyzer import analyze_error

st.set_page_config(page_title="K8s Doctor AI", page_icon="🩺")

st.title("🩺 K8s Doctor AI")
st.subheader("Kubernetes Log Analyzer")

# Sample Logs Data
log_options = {
    "Select an example...": "",
    "Disk Pressure": "Events:\nType Reason Age From Message\nWarning OutOfDisk 12m kubelet Node node-01 disk pressure",
    "CrashLoopBackOff": "NAME READY STATUS RESTARTS AGE\nmy-app-76d7f9556-abcde 0/1 CrashLoopBackOff 12 5m"
}

selected_option = st.selectbox("Or choose a sample log:", list(log_options.keys()))

# Ek hi baar input field define karo
log_input = st.text_area(
    "Paste your kubectl logs here:", 
    value=log_options[selected_option] if selected_option != "Select an example..." else "", 
    height=200
)

if st.button("Analyze"):
    if log_input:
        with st.spinner('Analyzing...'):
            issue = detect_issue(log_input)
            issue_to_analyze = issue if issue else log_input
            details = analyze_error(issue_to_analyze)
            
            st.success("Analysis Complete!")
            st.write(f"**Issue:** {issue if issue else 'Unknown'}")
            st.write(f"**Cause:** {details['cause']}")
            st.write("**Recommended Fixes:**")
            for fix in details['remediation']:
                st.info(fix)
    else:
        st.warning("Please paste some logs to analyze.")
