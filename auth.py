import streamlit as st
import subprocess

# Function to load credentials from Streamlit secrets
def load_credentials():
    credentials = st.secrets["credentials"]
    return credentials

def main():
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
                st.success('Logged in successfully!')
                # Execute main.py using subprocess
                subprocess.run(['streamlit', 'run', 'main.py'])
            else:
                st.error('Incorrect password')
        else:
            st.error('Username not found')

if __name__ == '__main__':
    main()
