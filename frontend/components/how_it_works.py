import streamlit as st

def show_how_it_works():

    st.write("")
    st.write("")

    st.markdown(
        """
        <h2 style="text-align:center;color:#F4C430;">
        How It Works
        </h2>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(
            """
### Step 1

Create your investment profile.

Tell us about your income, savings and goals.
"""
        )

    with col2:
        st.success(
            """
### Step 2

Run investment simulations.

Experiment with SIP, returns and inflation.
"""
        )

    with col3:
        st.success(
            """
### Step 3

Receive AI insights.

Understand how to improve your financial future.
"""
        )