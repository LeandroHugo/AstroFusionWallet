// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimeLockWallet {
    address payable public owner;
    uint256 public lockTime;

    event Deposited(address indexed from, uint256 amount);
    event Withdrawn(address indexed to, uint256 amount);
    event LockTimeUpdated(uint256 newLockTime);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = payable(msg.sender);
    }

    // Deposit funds into the contract
    function deposit() external payable {
        _deposit(msg.sender, msg.value);
    }

    // Internal deposit function
    function _deposit(address sender, uint256 amount) internal {
        require(amount > 0, "No funds sent");
        emit Deposited(sender, amount);
    }

    // Set the lock time
    function setLockTime(uint256 _lockTimeInSeconds) external onlyOwner {
        lockTime = block.timestamp + _lockTimeInSeconds;
        emit LockTimeUpdated(lockTime);
    }

    // Withdraw funds if the current time is greater than the lock time
    function withdraw() external onlyOwner {
        require(block.timestamp >= lockTime, "Funds are locked");
        uint256 amount = address(this).balance;
        owner.transfer(amount);
        emit Withdrawn(owner, amount);
    }

    // Deadman switch to transfer ownership
    function transferOwnership(address payable newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Transfer funds to another address
    function transferFunds(address payable recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient is the zero address");
        require(amount <= address(this).balance, "Insufficient funds");
        recipient.transfer(amount);
    }

    // Fallback function to deposit funds
    receive() external payable {
        _deposit(msg.sender, msg.value);
    }
}
