from brownie import accounts, config, TestToken

initial_supply = 100000000000000000000
token_name = 'TestToken'
token_symbol = 'TT'


def main():
    account = accounts[0]
    erc20 = TestToken.deploy(initial_supply, {"from": account})