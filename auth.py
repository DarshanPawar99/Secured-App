import streamlit as st

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
    st.write(f"Hello, {st.session_state['username']}!")

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
