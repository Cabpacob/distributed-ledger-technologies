// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Kekerium is ERC20 {
    constructor(uint256 initialSupply) payable ERC20("KEKERIUM", "KEK") {
        _mint(msg.sender, initialSupply);
    }
}

