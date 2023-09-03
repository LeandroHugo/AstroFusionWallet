// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.0/contracts/token/ERC20/IERC20.sol";

contract PremiumTimeLock {
    address public beneficiary;
    uint256 public releaseTime;
    IERC20 public token;

    constructor(IERC20 _token, address _beneficiary, uint256 _releaseTime) {
        require(_beneficiary != address(0), "Invalid beneficiary");
        require(_releaseTime > block.timestamp, "Release time in the past");

        token = _token;
        beneficiary = _beneficiary;
        releaseTime = _releaseTime;
    }

    function release() public {
        require(msg.sender == beneficiary, "Not beneficiary");
        require(block.timestamp >= releaseTime, "Not yet");

        uint256 amount = token.balanceOf(address(this));
        require(amount > 0, "No tokens");

        token.transfer(beneficiary, amount);
    }
}
