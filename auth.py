import streamlit as st
import time
from streamlit.components.v1 import html

# Function to load credentials from Streamlit secrets
def load_credentials():
    credentials = st.secrets["credentials"]
    return credentials

# Function for the login page
def login():
    st.title("Login")

    # Load credentials from Streamlit secrets
    credentials = load_credentials()
    usernames = credentials['usernames']
    passwords = credentials['passwords']

    # Input fields for username and password
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Login button
    if st.button('Login'):
        if username in usernames:
            index = usernames.index(username)
            if password == passwords[index]:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username
                st.experimental_rerun()
            else:
                st.error('Incorrect password')
        else:
            st.error('Username not found')

# Function for the main app
def main_app():
    st.title("Main App")
    username = st.session_state['username']
    st.write(f"Hello, {username}!")
    show_toast(f"Hello, {username}!")

# Function to show toast notification
def show_toast(message):
    toast = f"""
    <script>
    const toast = document.createElement('div');
    toast.innerHTML = '{message}';
    toast.style.position = 'fixed';
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.backgroundColor = '#333';
    toast.style.color = '#fff';
    toast.style.padding = '10px';
    toast.style.borderRadius = '5px';
    toast.style.zIndex = '9999';
    toast.style.opacity = '1';
    toast.style.transition = 'opacity 0.5s ease';

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 500);
    }, 2000);
    </script>
    """
    html(toast)

# Main function to control the app flow
def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        main_app()
    else:
        login()

if __name__ == '__main__':
    main()
