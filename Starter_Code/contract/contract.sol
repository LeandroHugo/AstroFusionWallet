pragma solidity ^0.5.8;

contract AdvancedTimeLockWallet {
    address payable public owner;
    address payable public backupOwner; // For deadman switch
    address public secondaryAddress; // For 2FA

    uint public balance;
    uint public lockTime;
    uint public lastCheckIn = now;
    uint public deadmanSwitchTime = 365 days; // Default 1 year

    bool public pendingWithdrawal = false;

    event Deposited(address from, uint amount, uint balance);
    event Withdrawn(address to, uint amount, uint balance);
    event LockTimeUpdated(uint newLockTime);
    event CheckIn(address owner);
    event SecondaryApproval(address secondary);

    constructor(address _secondaryAddress, address payable _backupOwner) public {
        owner = msg.sender;
        secondaryAddress = _secondaryAddress;
        backupOwner = _backupOwner;
    }

    function depositAndSetLockTime(uint _lockTimeInSeconds) public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;

        if (balance == msg.value) { // Check if this is the initial deposit
            lockTime = now + _lockTimeInSeconds;
            emit LockTimeUpdated(lockTime);
        }

        emit Deposited(msg.sender, msg.value, balance);
    }

    function requestWithdrawal() public {
        require(msg.sender == owner, "Only the owner can request withdrawal");
        require(now >= lockTime, "Wallet is locked");
        pendingWithdrawal = true;
    }

    function approveWithdrawal() public {
        require(msg.sender == secondaryAddress, "Only the secondary address can approve withdrawal");
        require(pendingWithdrawal, "No pending withdrawal to approve");

        uint amount = balance;
        balance = 0;
        owner.transfer(amount);
        pendingWithdrawal = false;
        emit Withdrawn(owner, amount, 0);
    }

    function updateLockTime(uint _lockTimeInSeconds) public {
        require(msg.sender == owner, "Only the owner can update lock time");
        lockTime = now + _lockTimeInSeconds;
        emit LockTimeUpdated(lockTime);
    }

    function checkIn() public {
        require(msg.sender == owner, "Only the owner can check in");
        lastCheckIn = now;
        emit CheckIn(owner);
    }

    function deadmanSwitch() public {
        require(msg.sender == backupOwner, "Only the backup owner can trigger the deadman switch");
        require(now >= lastCheckIn + deadmanSwitchTime, "Owner has checked in recently");
        owner = backupOwner;
    }

    function() external payable {
        depositAndSetLockTime(0);
    }
}
