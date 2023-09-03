pragma solidity ^0.5.0;

contract AdvancedTimeLockWallet {
    address payable public owner;
    address public admin; // New admin role
    address public secondaryAddress; // For 2FA

    uint public balance;
    uint public lockTime;
    uint public lastCheckIn = now;
    uint public deadmanSwitchTime = 365 days; // Default 1 year

    bool public pendingWithdrawal = false;

    event Deposited(address indexed from, uint amount, uint balance, string message);
    event Withdrawn(address indexed to, uint amount, uint balance);
    event LockTimeUpdated(uint newLockTime);
    event CheckIn(address owner);
    event Transfer(address indexed from, address indexed to, uint amount, uint balance);

    constructor(address _secondaryAddress, address _admin) public {
        owner = msg.sender;
        secondaryAddress = _secondaryAddress;
        admin = _admin; // Initialize the admin
    }

    function setAdmin(address _admin) public {
        require(msg.sender == owner, "Only the owner can set the admin");
        admin = _admin;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value, balance, "");
    }

    function depositWithMessage(string memory message) public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value, balance, message);
    }

    function requestWithdrawal(uint amount) public {
        require(msg.sender == owner, "Only the owner can request withdrawal");
        require(now >= lockTime, "Wallet is locked");
        require(amount <= balance, "Insufficient balance");
        pendingWithdrawal = true;
    }

    function approveWithdrawal() public {
        require(msg.sender == secondaryAddress, "Only the secondary address can approve withdrawal");
        require(pendingWithdrawal, "No pending withdrawal to approve");

        uint amount = balance;
        balance = 0;
        owner.transfer(amount);
        pendingWithdrawal = false;
        emit Withdrawn(owner, amount, balance);
    }

    function updateLockTime(uint _lockTimeInSeconds) public {
        require(msg.sender == admin, "Only the admin can update lock time");
        lockTime = now + _lockTimeInSeconds;
        emit LockTimeUpdated(lockTime);
    }

    function checkIn() public {
        require(msg.sender == owner, "Only the owner can check in");
        lastCheckIn = now;
        emit CheckIn(owner);
    }

    function deadmanSwitch(address payable newOwner) public {
        require(msg.sender == owner, "Only the owner can use the deadman switch");
        owner = newOwner;
    }

    function transfer(address payable recipient, uint amount) public {
        require(msg.sender == owner, "Only the owner can transfer");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        recipient.transfer(amount);
        emit Transfer(owner, recipient, amount, balance);
    }

    function() external payable {
        deposit();
    }
}
