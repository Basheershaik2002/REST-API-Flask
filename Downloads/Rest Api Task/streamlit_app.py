import streamlit as st
import requests

BASE_URL = 'http://127.0.0.1:5000'

st.title("👤 User Management - Flask + Streamlit")

# Add user
st.subheader("➕ Add User")
username = st.text_input("Username")
email = st.text_input("Email")

if st.button("Add User"):
    res = requests.post(f"{BASE_URL}/users", json={'username': username, 'email': email})
    st.write(res.status_code, res.json())

# Update user
st.subheader("🔄 Update User Email")
update_username = st.text_input("Update User (username)")
new_email = st.text_input("New Email")

if st.button("Update User"):
    res = requests.put(f"{BASE_URL}/users/{update_username}", json={'email': new_email})
    st.write(res.status_code, res.json())

# Get all users
st.subheader("📥 Get All Users")
if st.button("Fetch All Users"):
    res = requests.get(f"{BASE_URL}/users")
    st.json(res.json())
