
---

# AdvancedTimeLockWallet Contract Guide

The `AdvancedTimeLockWallet` is a smart contract designed to securely hold funds with a time lock feature and secondary approval. It includes functionalities such as deposits, withdrawals, transfers, and a deadman switch.

## Contract Structure

- **State Variables**:
  - `owner`: The main owner of the contract.
  - `admin`: An administrative role with specific permissions.
  - `secondaryAddress`: A secondary address required for two-factor authentication (2FA) on withdrawals.
  - `balance`: Current balance of the contract.
  - `lockTime`: Time until which the funds are locked.
  - `lastCheckIn`: The last time the owner checked in.
  - `deadmanSwitchTime`: Time after which the deadman switch can be activated.
  - `pendingWithdrawal`: Flag to indicate if a withdrawal has been requested.

- **Events**:
  - `Deposited`: Triggered when funds are deposited.
  - `Withdrawn`: Triggered when funds are withdrawn.
  - `LockTimeUpdated`: Triggered when the lock time is updated.
  - `CheckIn`: Triggered when the owner checks in.
  - `Transfer`: Triggered when funds are transferred to another address.

## Key Functions

1. **Constructor**:
   Initializes the contract with a secondary address and an admin address.

2. **setAdmin**:
   Allows the owner to set a new admin.

3. **deposit** & **depositWithMessage**:
   Allows anyone to deposit funds into the contract. The `depositWithMessage` function also logs a custom message with the deposit event.

4. **requestWithdrawal**:
   The owner can request a withdrawal of a specific amount. The withdrawal has to be approved by the secondary address.

5. **approveWithdrawal**:
   The secondary address can approve a withdrawal after it has been requested.

6. **updateLockTime**:
   The admin can update the lock time of the contract.

7. **checkIn**:
   The owner can check in, which resets the `lastCheckIn` state variable.

8. **deadmanSwitch**:
   The owner can transfer ownership to a new owner using the deadman switch. 

9. **transfer**:
   The owner can transfer funds to another address.

10. **Fallback function**:
   Allows the contract to receive funds.

---

## Usage Guide

1. **Deployment**:
   Deploy the contract by providing a secondary address and an admin address.

2. **Deposits**:
   Anyone can deposit funds into the contract using the `deposit` or `depositWithMessage` functions.

3. **Withdrawals**:
   - The owner requests a withdrawal using `requestWithdrawal`.
   - The secondary address approves the withdrawal using `approveWithdrawal`.

4. **Transfers**:
   The owner can send funds to any Ethereum address using the `transfer` function.

5. **Lock Time**:
   The admin can update the lock time using the `updateLockTime` function.

6. **Deadman Switch**:
   If required, the owner can transfer ownership to a new address using the `deadmanSwitch` function.

---
