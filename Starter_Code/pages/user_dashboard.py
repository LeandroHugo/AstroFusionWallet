# pages/user_dashboard.py

import streamlit as st
from web3 import Web3

# Assuming you've set up the web3 connection and contract instance in a shared module
from shared import web3, contract

def app():
    st.title("User Dashboard")

    if st.button("Deposit Funds"):
        tx_hash = contract.functions.deposit().transact({'from': web3.eth.accounts[0], 'value': web3.toWei(1, 'ether')})
        st.write(f"Deposited 1 Ether! Transaction hash: {tx_hash.hex()}")

    balance = contract.functions.balance().call()
    st.write(f"Current Balance: {web3.fromWei(balance, 'ether')} Ether")

    if st.button("Withdraw Funds"):
        tx_hash = contract.functions.withdraw().transact({'from': web3.eth.accounts[0]})
        st.write(f"Withdrew funds! Transaction hash: {tx_hash.hex()}")
