import streamlit as st

from utils.auth import hash_password
from database.database import add_user, get_user


def show_signup():

    st.title("📝 Create Account")
    st.write("Start your investment journey today!")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

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

    monthly_expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=0.0,
        step=1000.0
    )

    monthly_savings = st.number_input(
        "Monthly Savings (₹)",
        min_value=0.0,
        step=1000.0
    )

    financial_goal = st.selectbox(
        "Financial Goal",
        [
            "Retirement",
            "House",
            "Education",
            "Wealth Creation",
            "Emergency Fund"
        ]
    )

    investment_experience = st.selectbox(
        "Investment Experience",
        [
            "Beginner",
            "Intermediate",
            "Experienced"
        ]
    )

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        if not name or not email or not password:
            st.error("Please fill all required fields.")
            return

        if get_user(email):
            st.error("Email already registered.")
            return

        hashed_password = hash_password(password)

        add_user(
            name,
            email,
            hashed_password,
            age,
            income,
            risk,
            monthly_expenses,
            monthly_savings,
            financial_goal,
            investment_experience
        )

        st.success("🎉 Account Created Successfully!")

        st.session_state.page = "login"

        st.rerun()

    st.divider()

    if st.button(
        "Already have an account?",
        use_container_width=True
    ):
        st.session_state.page = "login"
        st.rerun()