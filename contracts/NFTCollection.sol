// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts-upgradeable/contracts/token/ERC721/ERC721Upgradeable.sol";
import "@openzeppelin/contracts-upgradeable/contracts/token/ERC721/extensions/ERC721BurnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/contracts/access/OwnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/contracts/utils/CountersUpgradeable.sol";

contract NFTCollection is
    Initializable,
    ERC721Upgradeable,
    ERC721BurnableUpgradeable,
    OwnableUpgradeable
{
    using CountersUpgradeable for CountersUpgradeable.Counter;

    CountersUpgradeable.Counter private _tokenIdCounter;

    uint256 public i;

    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() initializer {}

    function initialize() public initializer {
        __ERC721_init("NFTCollection", "NFTC");
        __ERC721Burnable_init();
        __Ownable_init();
        i++;
    }

    function safeMint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    function viewI() public view returns (uint256) {
        return i;
    }
}
