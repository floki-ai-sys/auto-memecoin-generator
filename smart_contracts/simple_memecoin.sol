// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Memecoin {
    string public name = "Memecoin";
    string public symbol = "MEME";
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;

    constructor(uint256 _totalSupply) {
        totalSupply = _totalSupply;
        balanceOf[msg.sender] = _totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        return true;
    }
}
