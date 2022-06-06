from web3 import Web3

url = 'https://mainnet.infura.io/v3/b81798c5f38b408ab6270d6b9c839ded'
web = Web3(Web3.HTTPProvider(url))

def check_balance(wallet_address):
    return web.eth.getBalance(wallet_address)

def make_transaction(sender_wallet, receiver_wallet, private_key, amount):
    nonce = web.eth.getTransactionCount(sender_wallet)
    tx = {
        'nonce': nonce,
        'to': receiver_wallet,
        'value': amount
    }
    signed_tx = web.eth.account.signTransaction(tx, private_key)
    return web.eth.sendRawTransaction(signed_tx.rawTransaction)

web.eth.is_addre
    