import streamlit as st
from web3 import Web3

# Connect to your Ethereum node
GANACHE_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# Use the ABI provided (the one you shared previously)
ABI = [
	{
		"constant": False,
		"inputs": [],
		"name": "approveWithdrawal",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "checkIn",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "deadmanSwitch",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_lockTimeInSeconds",
				"type": "uint256"
			}
		],
		"name": "depositAndSetLockTime",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "requestWithdrawal",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_secondaryAddress",
				"type": "address"
			},
			{
				"internalType": "address payable",
				"name": "_backupOwner",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "CheckIn",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "balance",
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
				"indexed": False,
				"internalType": "address",
				"name": "secondary",
				"type": "address"
			}
		],
		"name": "SecondaryApproval",
		"type": "event"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_lockTimeInSeconds",
				"type": "uint256"
			}
		],
		"name": "updateLockTime",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			}
		],
		"name": "Withdrawn",
		"type": "event"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "backupOwner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "balance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "deadmanSwitchTime",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "lastCheckIn",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "lockTime",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "pendingWithdrawal",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "secondaryAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]
# ABI array goes here

# Contract address after you've deployed it
contract_address = '0x433f73771c6532F5168a71bb3f83A1D7aE612cB4'  # Replace with your actual address
contract = web3.eth.contract(address=contract_address, abi=ABI)

def main():
    st.title("Advanced Cryptocurrency Wallet")

    # Display the contract owner
    st.subheader("Contract Owner")
    owner = contract.functions.owner().call()
    st.write(owner)

    # Display the backup owner
    st.subheader("Backup Owner")
    backup_owner = contract.functions.backupOwner().call()
    st.write(backup_owner)

    # Display the secondary address for 2FA
    st.subheader("Secondary Address (2FA)")
    secondary_address = contract.functions.secondaryAddress().call()
    st.write(secondary_address)

    # Deposit Ether
    st.subheader("Deposit Ether")
    deposit_amount = st.text_input("Amount to deposit (in Ether):", value="0")
    if st.button("Deposit"):
        tx_hash = contract.functions.depositAndSetLockTime(0).transact({
            'from': web3.eth.accounts[0], 
            'value': web3.toWei(deposit_amount, 'ether')
        })
        st.write(f"Deposited {deposit_amount} Ether! Transaction hash: {tx_hash.hex()}")

    # Request Withdrawal (Owner triggers this, then secondary approves)
    st.subheader("Request Withdrawal")
    if st.button("Request Withdrawal"):
        tx_hash = contract.functions.requestWithdrawal().transact({'from': web3.eth.accounts[0]})
        st.write(f"Withdrawal requested! Awaiting secondary approval. Transaction hash: {tx_hash.hex()}")

    # Secondary Approves Withdrawal
    st.subheader("Secondary Address Approves Withdrawal")
    if st.button("Approve Withdrawal"):
        tx_hash = contract.functions.approveWithdrawal().transact({'from': web3.eth.accounts[0]})
        st.write(f"Withdrawal approved by secondary address! Transaction hash: {tx_hash.hex()}")

    # Display Current Balance of Ether
    st.subheader("Ether Balance")
    balance = web3.fromWei(web3.eth.getBalance(contract_address), 'ether')
    st.write(f"Current Balance: {balance} Ether")

    # Transfer Ownership
    st.subheader("Transfer Ownership")
    new_owner_address = st.text_input("New owner address:")
    if st.button("Transfer Ownership"):
        tx_hash = contract.functions.transferOwnership(new_owner_address).transact({'from': web3.eth.accounts[0]})
        st.write(f"Ownership transferred! Transaction hash: {tx_hash.hex()}")

    # Deadman switch functionality
    st.subheader("Deadman Switch")
    if st.button("Claim After Inactivity"):
        tx_hash = contract.functions.deadmanSwitch().transact({'from': web3.eth.accounts[0]})
        st.write(f"Ownership claimed by backup owner due to inactivity! Transaction hash: {tx_hash.hex()}")

    # (Optional) Add more functionalities as needed...

if __name__ == "__main__":
    main()
