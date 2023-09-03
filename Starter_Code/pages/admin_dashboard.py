# pages/admin_dashboard.py

import streamlit as st
from shared import web3, contract

def app():
    st.title("Admin Dashboard")

    new_lock_time = st.text_input("Set New Lock Time (in seconds):")
    if st.button("Update Lock Time"):
        tx_hash = contract.functions.setLockTime(int(new_lock_time)).transact({'from': web3.eth.accounts[0]})
        st.write(f"Lock Time Updated! Transaction hash: {tx_hash.hex()}")

    lock_time = contract.functions.lockTime().call()
    st.write(f"Current Lock Time: {lock_time} seconds")
