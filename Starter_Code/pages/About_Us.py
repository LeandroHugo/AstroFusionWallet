import streamlit as st

def run():
    # Page Title & Description
    st.title('Advanced TimeLock Wallet ⏳')
    st.write("Dive into the world of secure digital asset management with cutting-edge features tailored for you.")
    
    # Animated Header or Logo
    # Uncomment and use your logo
    # st.image("path_to_your_logo.png", use_column_width=True)

    # Feature Highlights with Icons
    features = {
        "🔒 Security": "Top-tier security features ensuring the safety of digital assets.",
        "⏲️ TimeLock": "Lock assets until a specific time. They remain untouched until the timer runs out.",
        "🔥 Deadman Switch": "Transfer assets to a trusted entity after prolonged inactivity."
    }
    
    cols = st.columns(3)
    for i, (icon, feature) in enumerate(features.items()):
        with cols[i]:
            st.write(f"### {icon}")
            st.write(feature)

    # User Testimonials in Expanders
    st.subheader("🗣️ User Testimonials")
    with st.expander("Alex's Review"):
        st.write("""
        "The Advanced TimeLock Wallet revolutionized my crypto management. The Deadman Switch is a lifesaver!"
        """)
    with st.expander("Samantha's Thoughts"):
        st.write("""
        "My digital assets have never felt safer. The UI is intuitive, and TimeLock is a feature I never knew I needed."
        """)

    # Quick Navigation
    st.subheader("🚀 Quick Navigation")
    dashboard_selection = st.radio("", ["User Dashboard", "Admin Dashboard"])
    if st.button("Navigate"):
        # Logic to handle navigation
        st.write(f"Navigating to {dashboard_selection}...")

    # FAQ Chatbot Section
    st.header("💬 FAQ Chatbot")
    user_input = st.text_input("Ask about TimeLock, Deadman Switch, and more!")
    if st.button("Submit"):
        response = faq_bot_response(user_input)
        st.write(f"🤖: {response}")

    # Pre-defined FAQ Section in an Expander
    faq_expander = st.expander("📜 Commonly Asked Questions")
    with faq_expander:
        selected_question = st.selectbox("Choose a query:", list(faq_dict.keys()))
        st.write(f"**Question:** {selected_question}")
        st.write(f"**Answer:** {faq_dict[selected_question]}")

    # Footer
    st.write("---")
    st.write("""
    [Terms of Service](#) | [Privacy Policy](#) | [Support](#)
    """)  # Replace '#' with actual links

# Basic FAQ bot logic using predefined Q&A
def faq_bot_response(user_input):
    faq_responses = {
        "timelock": "The TimeLock feature allows you to lock your assets until a specified time has passed.",
        "deadman switch": "The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.",
        "deposit funds": "Navigate to the User Dashboard and use the deposit function."
    }
    for key, value in faq_responses.items():
        if key in user_input.lower():
            return value
    return "Sorry, I can't assist with that right now. Maybe rephrase or ask another question?"

# Pre-defined FAQs
faq_dict = {
    "How does the TimeLock feature work?": "The TimeLock feature allows you to lock your assets until a specified time has passed.",
    "What is the Deadman Switch?": "The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.",
    "How can I deposit funds into the wallet?": "Navigate to the User Dashboard and use the deposit function."
}

if __name__ == '__main__':
    run()
