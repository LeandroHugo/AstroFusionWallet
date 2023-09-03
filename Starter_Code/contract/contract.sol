// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract AdvancedCryptocurrencyWallet {
    address public owner;
    address public backupOwner; // For deadman switch
    address public secondaryAddress; // For 2FA

    uint256 public lastActivity; // Timestamp of the last activity
    uint256 public deadmanSwitchTimeout = 365 days; // Default 1 year

    struct TokenDetails {
        uint256 balance;
        uint256 lockTime;
        bool secondaryApproval; // Approval from the secondary address
    }

    mapping(address => TokenDetails) public tokenBalances;

    event Deposited(address indexed from, address indexed token, uint256 amount);
    event Withdrawn(address indexed to, address indexed token, uint256 amount);
    event LockTimeUpdated(address indexed token, uint256 newLockTime);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event SecondaryApprovalGranted(address indexed token);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        lastActivity = block.timestamp;
        _;
    }

    modifier onlyBackupOwner() {
        require(msg.sender == backupOwner, "Not the backup owner");
        _;
    }

    modifier onlySecondary() {
        require(msg.sender == secondaryAddress, "Not the secondary address");
        _;
    }

    constructor(address _backupOwner, address _secondaryAddress) {
        require(_backupOwner != address(0), "Backup owner cannot be zero address");
        require(_secondaryAddress != address(0), "Secondary address cannot be zero address");

        owner = msg.sender;
        backupOwner = _backupOwner;
        secondaryAddress = _secondaryAddress;

        lastActivity = block.timestamp;
    }

    function depositEther() external payable {
        require(msg.value > 0, "No ETH sent");
        tokenBalances[address(0)].balance += msg.value;
        emit Deposited(msg.sender, address(0), msg.value);
    }

    function depositToken(address tokenAddress, uint256 amount) external {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "No tokens to deposit");
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
        tokenBalances[tokenAddress].balance += amount;
        emit Deposited(msg.sender, tokenAddress, amount);
    }

    function grantSecondaryApproval(address tokenAddress) external onlySecondary {
        tokenBalances[tokenAddress].secondaryApproval = true;
        emit SecondaryApprovalGranted(tokenAddress);
    }

    function withdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(block.timestamp >= tokenBalances[tokenAddress].lockTime, "Funds are locked");
        require(tokenBalances[tokenAddress].secondaryApproval, "Secondary approval required for withdrawal");
        require(amount <= tokenBalances[tokenAddress].balance, "Insufficient funds");

        tokenBalances[tokenAddress].balance -= amount;

        if(tokenAddress == address(0)) {
            payable(owner).transfer(amount);
        } else {
            IERC20(tokenAddress).transfer(owner, amount);
        }
        emit Withdrawn(owner, tokenAddress, amount);
    }

    function setLockTime(address tokenAddress, uint256 _lockTimeInSeconds) external onlyOwner {
        tokenBalances[tokenAddress].lockTime = block.timestamp + _lockTimeInSeconds;
        emit LockTimeUpdated(tokenAddress, tokenBalances[tokenAddress].lockTime);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function claimAfterInactivity() external onlyBackupOwner {
        require(block.timestamp > lastActivity + deadmanSwitchTimeout, "Owner is still active");
        emit OwnershipTransferred(owner, backupOwner);
        owner = backupOwner;
    }

    function balanceOf(address tokenAddress) external view returns (uint256) {
        return tokenBalances[tokenAddress].balance;
    }
}
