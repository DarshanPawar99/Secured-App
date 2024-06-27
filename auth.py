import streamlit as st
import toml
import subprocess

# Function to load credentials from secrets.toml
def load_credentials(file_path):
    credentials = toml.load(file_path)
    return credentials

def main():
    st.title("Login")

    # Load credentials from secrets.toml
    credentials = load_credentials('secrets.toml')
    usernames = credentials['credentials']['usernames']
    passwords = credentials['credentials']['passwords']

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
