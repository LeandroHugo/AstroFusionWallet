import streamlit as st
from web3 import Web3
import json

# 1. Setup and Contract Initialization

GANACHE_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

ABI = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "Deposited",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "newLockTime",
				"type": "uint256"
			}
		],
		"name": "LockTimeUpdated",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "Withdrawn",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "balance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "deposit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "lockTime",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_lockTimeInSeconds",
				"type": "uint256"
			}
		],
		"name": "setLockTime",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "recipient",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFunds",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]

# As provided in the initial code

contract_address = '0x88Dae24EbC7F8a30c7eBeF7FEF6b4dcCD283e3d1'
contract = web3.eth.contract(address=contract_address, abi=ABI)

# 2. User Dashboard

st.title("TimeLockWallet Dashboard")

# Deposit Funds
if st.button("Deposit Funds"):
    # Here, you'd need to specify the address from which you're sending and the amount.
    # This is a basic example; in a real-world scenario, you'd want to have input fields
    # for the user to specify the amount and perhaps even the sender's address.
    tx_hash = contract.functions.deposit().transact({'from': web3.eth.accounts[0], 'value': web3.toWei(1, 'ether')})
    st.write(f"Deposited 1 Ether! Transaction hash: {tx_hash.hex()}")

# Display Current Balance
balance = contract.functions.balance().call()
st.write(f"Current Balance: {web3.fromWei(balance, 'ether')} Ether")

# Withdraw Funds
if st.button("Withdraw Funds"):
    tx_hash = contract.functions.withdraw().transact({'from': web3.eth.accounts[0]})
    st.write(f"Withdrew funds! Transaction hash: {tx_hash.hex()}")

# 3. Admin Dashboard

st.title("Admin Dashboard")

# Set Lock Time
new_lock_time = st.text_input("Set New Lock Time (in seconds):")
if st.button("Update Lock Time"):
    tx_hash = contract.functions.depositAndSetLockTime(int(new_lock_time)).transact({'from': web3.eth.accounts[0]})
    st.write(f"Lock Time Updated! Transaction hash: {tx_hash.hex()}")

# Display Current Lock Time
lock_time = contract.functions.lockTime().call()
st.write(f"Current Lock Time: {lock_time} seconds")

# 4. Transaction History

st.title("Transaction History")

# Listen to events (for simplicity, we're just fetching past events)
deposited_events = contract.events.Deposited.getLogs()
for event in deposited_events:
    st.write(f"Deposited {web3.fromWei(event['amount'], 'ether')} Ether from {event['from']}")

withdrawn_events = contract.events.Withdrawn.getLogs()
for event in withdrawn_events:
    st.write(f"Withdrew {web3.fromWei(event['amount'], 'ether')} Ether to {event['to']}")

lock_time_updated_events = contract.events.LockTimeUpdated.getLogs()
for event in lock_time_updated_events:
    st.write(f"Lock Time Updated to {event['newLockTime']} seconds")

# ... You can add other event listeners similarly ...
