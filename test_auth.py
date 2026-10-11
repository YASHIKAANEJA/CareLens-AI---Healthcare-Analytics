import streamlit as st
from auth import sign_up, sign_in


st.title("CareLens Authentication Test")

email = st.text_input("Email")
password = st.text_input(
    "Password",
    type="password"
)

if st.button("Create Account"):

    try:
        response = sign_up(email, password)

        st.success(
            "Account created. Check your email if confirmation is enabled."
        )

    except Exception as e:
        st.error(str(e))


if st.button("Login"):

    try:
        if sign_in(email, password):
            st.success("Login successful!")

    except Exception as e:
        st.error(str(e))