import streamlit as st

def run():

    st.title('Advanced TimeLock Wallet 🆘 Support')

    # Columns for FAQs and Troubleshooting
    col1, col2 = st.columns(2)

    # FAQs in Column 1
    with col1:
        st.subheader("🤔 FAQs")
        faq_expander = st.expander("Click to view")
        with faq_expander:
            st.write("""
            **1. How does the Advanced TimeLock Wallet feature work?**
            Lock your Ethereum assets until a specified time as per the contract's conditions.

            **2. What's the Deadman Switch in our contract?**
            A contract event triggered after a set inactivity duration, transferring funds to a designated address.

            **3. How to deposit into the Advanced TimeLock Wallet?**
            Use the contract's deposit function. Always verify the contract's address before transactions.
            """)

    # Troubleshooting in Column 2
    with col2:
        st.subheader("🛠️ Troubleshooting")
        troubleshoot_expander = st.expander("Click for common solutions")
        with troubleshoot_expander:
            st.write("""
            **Issue**: Can't access Ethereum after timer expiration.
            **Solution**: Ensure correct contract interaction and adherence to conditions. Contact support if persistent.

            **Issue**: Deadman Switch non-activation.
            **Solution**: Confirm contract conditions and surpassing of inactivity period. Set up the switch as instructed.
            """)

    # Contact Information
    st.subheader("📞 Contact Information")
    st.write("""
    - **Email**: [support@advancedtimelockwallet.com](mailto:support@advancedtimelockwallet.com)
    - **Phone**: +1 (123) 456-7890
    - **Live Chat**: [Start a chat](#)
    """)

    # Guides & Tutorials
    st.subheader("📚 Guides & Tutorials")
    st.write("Explore our detailed video tutorials and guides:")
    guide_links = {
        "Understanding Advanced TimeLock Wallet Features": "#",
        "Configuring the Deadman Switch": "#",
        "Efficiently Depositing and Withdrawing Funds": "#"
    }
    for guide, link in guide_links.items():
        st.write(f"- [{guide}]({link})")

    # Feedback Form in an Expander
    feedback_expander = st.expander("💌 Feedback & Issue Reporting")
    with feedback_expander:
        st.write("Help us refine our service. Share your feedback or report challenges.")
        feedback = st.text_area("Write here...")
        if st.button("Send Feedback"):
            # Logic to handle the feedback, e.g., sending an email or storing in a database
            st.success("Thanks for your input! We appreciate it.")

if __name__ == '__main__':
    run()
