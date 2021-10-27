from brownie import SimpleStorage, accounts, config


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    # simpleStorage = SimpleStorage.deploy({"from": accounts[0]})
    simpleStorage = SimpleStorage.deploy({"from": account}, publish_source=True)
    print(simpleStorage.retrieve())
    # storeTransaction = simpleStorage.store(77, {"from": accounts[0]})
    storeTransaction = simpleStorage.store(77, {"from": account})
    storeTransaction.wait(1)
    print(simpleStorage.retrieve())
    # SimpleStorage[-1]

def main():
    deploy()
