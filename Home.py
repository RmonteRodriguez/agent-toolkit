import streamlit as st

st.set_page_config(page_title="Agent Toolkit", page_icon="🧰", layout="centered")

st.title("🧰 Rmonte's Agent Toolkit")

st.info(
    "This toolkit is for internal use only. Tools provided here are for estimation and "
    "reference purposes. Always verify results before use in client-facing work. "
    "Agents must recieve permission from superviosr to use tools as they are not offical Progressive software"
)

st.markdown("### Available Tools")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Billing_Calculator.py", label="Renters Billing Calculator", icon="💰")
    st.caption("Estimate renters costs and billing breakdowns.")

with col2:
    st.page_link("pages/2_Jewelry_Tool.py", label=" Scheduled Jewelry Tool", icon="💍")
    st.caption("Reference tool for jewelry description")
