// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CurrencyExchangeOffice {
    
    address public owner;
    mapping (IERC20 => uint256) public exchangeRates;
    
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    constructor() payable {
        owner = msg.sender;
    }

    function setExchangeRate(address token, uint256 rate) external onlyOwner {
        require(rate > 0, "Exchange rate must be greater than zero");
        exchangeRates[IERC20(token)] = rate;
    }

    function buyToken(address token, uint256 amount) external payable {
        uint256 requiredEth = exchangeRates[IERC20(token)] * amount;
        require(msg.value == requiredEth, "Incorrect ETH amount");
        IERC20(token).transfer(msg.sender, amount);
    }

    function sellTokens(address token, uint256 amount) public {
        IERC20 erc20Token = IERC20(token);
        uint256 ethAmount = exchangeRates[erc20Token] * amount;
        require(ethAmount > 0, "Cannot sell tokens for zero Ether");
        require(address(this).balance >= ethAmount, "Contract has insufficient balance");

        erc20Token.transferFrom(msg.sender, address(this), amount);
        (bool success, ) = msg.sender.call{value: ethAmount}("");
        require(success, "Failed to send Ether");
    }

    function withdrawEther(address payable to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= address(this).balance, "Invalid amount");

        (bool success, ) = to.call{value: amount}("");
        require(success, "Failed to send Ether");
    }

    function withdrawTokens(address token, address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        IERC20 erc20Token = IERC20(token);
        uint256 contractTokenBalance = erc20Token.balanceOf(address(this));
        require(amount <= contractTokenBalance, "Invalid amount");

        erc20Token.transfer(to, amount);
    }
}

