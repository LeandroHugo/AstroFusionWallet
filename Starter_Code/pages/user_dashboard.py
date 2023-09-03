import streamlit as st
import time

# Dummy data for the sake of this example
USER_DATA = {
    "name": "John Doe",
    "wallet_address": "0x433f73771c6532F5168a71bb3f83A1D7aE612cB4",
    "balance": 100.5,
    "profile_pic": "https://www.w3schools.com/howto/img_avatar.png"
}

def validate_wallet(wallet_address):
    return wallet_address == USER_DATA["wallet_address"]

def run():
    st.title('Advanced User Dashboard 🚀')

    # Sidebar for user profile
    st.sidebar.header("Profile Overview 🧑")

    wallet_address = st.session_state.get("wallet_address", "")

    if wallet_address:  # If logged in
        st.sidebar.image(USER_DATA["profile_pic"], caption='Profile Picture', width=150)

        # Profile Picture Uploader with a Twist
        uploaded_file = st.sidebar.file_uploader("Change Profile Picture", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.sidebar.image(uploaded_file, caption='New Profile Pic', width=150)
        st.sidebar.write(f"**Name:** {USER_DATA['name']}")
        st.sidebar.write(f"**Wallet Address:** {USER_DATA['wallet_address']}")
        st.sidebar.markdown(f"**Balance:** `{USER_DATA['balance']} ETH` 💰")

        # Centralized Features
        st.markdown("### 🎉 Welcome Back!")
        st.write("Let's dive into your digital asset management journey.")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("Here's a peek into your recent activities.")
            # Display Transactions (dummy data)
            st.subheader('🔍 Recent Transactions')
            transactions = {
                'Date': ['2023-08-05', '2023-08-04', '2023-08-03'],
                'Type': ['Sent', 'Received', 'Sent'],
                'Amount': [-50, 100, -20],
                'Status': ['Completed', 'Completed', 'Pending']
            }
            st.table(transactions)

        with col2:
            st.subheader("📸 Profile Picture")
            st.write("Update or snap a new profile pic!")
            uploaded_photo = st.file_uploader("Upload a photo")
            camera_photo = st.camera_input("Or, take a photo!")
            
            if uploaded_photo or camera_photo:
                st.success("Photo updated successfully!")

        with st.expander("📖 Tips & Best Practices"):
            st.write("""
            **Security Tips:**
            - **Private Key:** Keep your private key confidential. Don't share or store online without encryption.
            - **Phishing:** Stay alert for phishing websites or misleading emails.
            - **Backup:** Ensure regular backups for your wallet data.

            **Wallet Efficiency:**
            - **Notifications:** Opt for notifications to stay updated with your wallet's status.

            **General Suggestions:**
            - Ensure double-checking of wallet addresses during transactions.
            """)

        if st.sidebar.button("Logout"):
            del st.session_state["wallet_address"]

    else:
        input_wallet_address = st.sidebar.text_input("Enter Wallet Address 🔒")
        if st.sidebar.button("Login"):
            if validate_wallet(input_wallet_address):
                st.session_state["wallet_address"] = input_wallet_address
                st.sidebar.success("Logged in successfully! ✅")
            else:
                st.sidebar.error("Invalid wallet address! ❌")

if __name__ == '__main__':
    run()
