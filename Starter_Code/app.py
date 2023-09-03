import streamlit as st
from web3 import Web3
import json

# Use Ganache for local blockchain development
GANACHE_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# Your contract ABI goes here
ABI = [
    #... (fill in the ABI of the AdvancedTimeLockWallet contract here)
]

# The contract address that you get after deploying your smart contract
contract_address = '0x433f73771c6532F5168a71bb3f83A1D7aE612cB4'

# Creating contract instance
contract = web3.eth.contract(address=contract_address, abi=ABI)

# Streamlit App
st.title('Advanced TimeLock Wallet')

# Set owner of the contract
owner = st.sidebar.text_input("Owner Address", value="0xYourAddress")

# If contract owner, show options
if owner == web3.eth.accounts[0]:
    st.header('Welcome Owner')

    # Deposit and Set Lock Time Simultaneously
    deposit_amount = st.text_input('Enter deposit amount:')
    lock_time = st.number_input('Enter lock time in seconds', step=1)
    if st.button('Deposit and Set Lock Time'):
        tx_hash = contract.functions.depositAndSetLockTime(int(lock_time)).transact({'from': owner, 'value': web3.toWei(float(deposit_amount), 'ether')})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.success(f"Deposit successful with lock time set. Transaction hash: {receipt['transactionHash'].hex()}")
        st.balloons()

    # Request Withdrawal
    request_withdrawal_amount = st.text_input('Enter withdrawal request amount:')
    if st.button('Request Withdrawal'):
        tx_hash = contract.functions.requestWithdrawal(web3.toWei(float(request_withdrawal_amount), 'ether')).transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.success(f"Withdrawal requested. Please have the secondary address approve the withdrawal. Transaction hash: {receipt['transactionHash'].hex()}")

    # Deadman Switch
    new_owner = st.text_input("Enter new owner address for Deadman Switch")
    if st.button('Activate Deadman Switch'):
        if Web3.isAddress(new_owner):  # Check if the address is valid
            tx_hash = contract.functions.deadmanSwitch(new_owner).transact({'from': owner})
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
            st.success(f"Deadman Switch activated. New owner is {new_owner}. Transaction hash: {receipt['transactionHash'].hex()}")
            st.balloons()
        else:
            st.error("The address entered is not valid. Please enter a valid Ethereum address.")
    
    # Display Balance
    balance = contract.functions.balance().call()
    st.write(f"Current Balance: {web3.fromWei(balance, 'ether')} ETH")

    # Display Lock Time
    lock_time_display = contract.functions.lockTime().call()
    st.write(f"Lock Time (UNIX timestamp): {lock_time_display}")

# Sidebar for secondary address operations
st.sidebar.header("Secondary Address Operations")
secondary = st.sidebar.text_input("Secondary Address", value="0xYourSecondaryAddress")
if secondary == web3.eth.accounts[1]:  # Assuming the secondary address is the second account in Ganache for this example
    if st.sidebar.button('Approve Withdrawal'):
        tx_hash = contract.functions.approveWithdrawal().transact({'from': secondary})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.success(f"Withdrawal approved by secondary address. Transaction hash: {receipt['transactionHash'].hex()}")
        st.balloons()

# Note: You might need to expand on this, add more features, or handle more edge cases based on your requirements.
