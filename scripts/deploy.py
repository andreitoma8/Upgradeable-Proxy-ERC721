from brownie import (
    Contract,
    accounts,
    config,
    NFTCollection,
    NFTCollectionV2,
    ProxyAdmin,
    TransparentUpgradeableProxy,
)
from scripts.helpful_scripts import encode_function_data, upgrade, get_account


def main():
    owner = accounts.add(config["wallets"]["from_key"])
    nft = NFTCollection.deploy({"from": owner})
    proxy_admin = ProxyAdmin.deploy({"from": owner})

    # initializer = NFTCollection.initialize
    encoded_initializer_function = encode_function_data(nft.initialize)

    proxy = TransparentUpgradeableProxy.deploy(
        nft.address,
        proxy_admin.address,
        encoded_initializer_function,
        {"from": owner},
    )

    proxy_nft = Contract.from_abi("NFTCollection", proxy.address, NFTCollection.abi)
    proxy_nft.safeMint(owner.address, {"from": owner})
    print(proxy_nft.viewI({"from": owner}))

    nftV2 = NFTCollectionV2.deploy({"from": owner})

    upgrade_tx = upgrade(
        owner,
        proxy,
        nftV2.address,
        proxy_admin,
    )

    proxy_nft = Contract.from_abi("NFTCollectionV2", proxy.address, NFTCollectionV2.abi)
    print(proxy_nft.viewI({"from": owner}))
    incremented_i = proxy_nft.incrementI({"from": owner})
    proxy_nft.safeMint(owner.address, {"from": owner})

    print(proxy_nft.viewI({"from": owner}))
