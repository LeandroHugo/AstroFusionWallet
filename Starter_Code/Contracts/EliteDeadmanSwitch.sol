// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract EliteDeadmanSwitch {
    address payable public owner;
    address payable public beneficiary;
    uint public lastCheckInTime;
    uint public inactivityPeriod;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this.");
        _;
    }

    constructor(address payable _beneficiary, uint _inactivityPeriod) {
        owner = payable(msg.sender);
        beneficiary = _beneficiary;
        inactivityPeriod = _inactivityPeriod;
        lastCheckInTime = block.timestamp;
    }

    function checkIn() public onlyOwner {
        lastCheckInTime = block.timestamp;
    }

    function releaseToBeneficiary() public {
        require(block.timestamp >= lastCheckInTime + inactivityPeriod, "Owner is still active!");
        beneficiary.transfer(address(this).balance);
    }
}
