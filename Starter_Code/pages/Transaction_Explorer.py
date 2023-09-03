import streamlit as st
import pandas as pd
import base64

def load_transaction_data(user_address):
    # Dummy data for demonstration purposes.
    # In reality, you'd fetch this data from your backend or the blockchain.
    data = {
        'Transaction Type': ['Deposit', 'Withdrawal', 'Transfer', 'Deposit'],
        'Date & Time': ['2023-08-05 10:10', '2023-08-06 11:15', '2023-08-07 14:20', '2023-08-08 09:05'],
        'Amount': [100, 50, 30, 150],
        'Status': ['Completed', 'Completed', 'Pending', 'Completed'],
        'Transaction Hash': ['0xabc...', '0xdef...', '0xghi...', '0xjkl...']
    }
    return pd.DataFrame(data)

def run():
    st.title('Advanced Transaction Explorer 📊')

    # Introduction
    st.write("""
    Dive into the detailed history of your transactions. Filter, analyze, and download your transactional data at your fingertips.
    """)

    # User wallet address input
    user_address = st.text_input('🔍 Enter your wallet address:', value='0x...')
    
    # Load transaction data
    df = load_transaction_data(user_address)

    # Filters in sidebar
    st.sidebar.header('Filters')
    transaction_type = st.sidebar.selectbox('Transaction Type', ['All'] + list(df['Transaction Type'].unique()))
    status_filter = st.sidebar.selectbox('Status', ['All'] + list(df['Status'].unique()))
    
    if transaction_type != 'All':
        df = df[df['Transaction Type'] == transaction_type]
    if status_filter != 'All':
        df = df[df['Status'] == status_filter]

    # Display data in an interactive table
    st.dataframe(df)

    # Additional Information
    st.subheader('📈 Transaction Analytics')
    st.write(f"**Total Transactions:** {len(df)}")
    st.write(f"**Total Deposited:** {df[df['Transaction Type'] == 'Deposit']['Amount'].sum()}")
    st.write(f"**Total Withdrawn:** {df[df['Transaction Type'] == 'Withdrawal']['Amount'].sum()}")

    # Export as CSV functionality
    if st.button('📥 Export as CSV'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Convert to bytes & base64 encoding
        href = f'<a href="data:file/csv;base64,{b64}" download="transaction_history.csv">Click Here to Download</a>'
        st.markdown(href, unsafe_allow_html=True)

    # Footer
    st.write("---")
    st.write("""
    [Terms of Service](#) | [Privacy Policy](#) | [Support](#)
    """)  # Replace '#' with actual links

if __name__ == '__main__':
    run()
