# app.py

import streamlit as st
from pages import home, admin_dashboard, transaction_history, help_support, user_dashboard

PAGES = {
    "Home": home,
    "Admin Dashboard": admin_dashboard,
    "User Dashboard": user_dashboard,
    "Transaction History": transaction_history,
    "Help & Support": help_support
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
