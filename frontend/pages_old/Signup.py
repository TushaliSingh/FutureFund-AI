import streamlit as st

st.set_page_config(page_title="Signup", page_icon="💰")

st.title("📝 Create Your FutureFund Account")

st.write("Start your investment journey by creating your account.")

name = st.text_input("Full Name")

email = st.text_input("Email Address")

password = st.text_input(
    "Password",
    type="password"
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=18
)

income = st.number_input(
    "Monthly Income (₹)",
    min_value=0.0,
    step=1000.0
)

risk = st.selectbox(
    "Risk Appetite",
    ["Low", "Medium", "High"]
)

if st.button("Create Account"):
    st.success("🎉 Account creation functionality coming next!")