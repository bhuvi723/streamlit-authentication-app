import streamlit as st
from auth.auth_utils import initialize_db, create_user, authenticate_user
from auth.auth_config import get_authenticator

# Initialize database
initialize_db()

authenticator = get_authenticator()
        
st.title('Streamlit App with Authentication')

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Select Page", menu)

def main():

    if choice == "Sign Up":
        st.subheader("Create an Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Sign Up"):
            if password == confirm_password:
                if authenticate_user(username, password):
                    st.error("User already exists")
                else:
                    create_user(username, password)
                    st.success("Account created successfully")
            else:
                st.error("Passwords do not match")

    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.login = True
                st.session_state.page = "myapp.py"
                st.success("Login successful")
                st.write(f"Welcome, {username}!")
                st.query_params(page="myapp")
                # st.experimental_rerun()
            else:
                st.error("Invalid username or password")


if __name__ == "__main__":
    main()
    