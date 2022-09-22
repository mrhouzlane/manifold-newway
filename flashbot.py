from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account
import secrets
from flashbots import flashbot
from flashbots.types import SignTx
from eth_account.account import Account
from web3 import Web3, HTTPProvider
from web3.types import TxParams, Wei
import os





def generate_private_key():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    # print ("SAVE BUT DO NOT SHARE THIS:", private_key)
    acct = Account.from_key(private_key)
    # print("Address:", acct.address)
    return private_key

ETH_SIGNATURE_KEY = generate_private_key()
ETH_PRIVATE_FROM = generate_private_key()
ETH_PRIVATE_TO = generate_private_key()

ETH_ACCOUNT_SIGNATURE: LocalAccount = Account.from_key((ETH_SIGNATURE_KEY))
ETH_ACCOUNT_FROM: LocalAccount = Account.from_key((ETH_PRIVATE_FROM))
ETH_ACCOUNT_TO: LocalAccount = Account.from_key((ETH_PRIVATE_TO))


print("Connecting to RPC......")
manifold_uri = "http://18.188.93.177:8545/"
web3_manifold = Web3(HTTPProvider(manifold_uri))
print(f"Conntected to Manifold RPC : {manifold_uri}")
web3_manifold.middleware_onion.add(construct_sign_and_send_raw_middleware(ETH_ACCOUNT_FROM))

flashbot(web3_manifold, ETH_ACCOUNT_SIGNATURE)

print(f"From account {ETH_ACCOUNT_FROM.address}: {web3_manifold.eth.get_balance(ETH_ACCOUNT_FROM.address)}")
print(f"To account {ETH_ACCOUNT_TO.address}: {web3_manifold.eth.get_balance(ETH_ACCOUNT_TO.address)}")

print("Sending request....")

params: TxParams = {
    "from": ETH_ACCOUNT_FROM.address,
    "to": ETH_ACCOUNT_TO.address,
    "value": web3_manifold.toWei("1.0", "gwei"),
    "gasPrice": web3_manifold.toWei("1.0", "gwei"),
    "nonce": web3_manifold.eth.get_transaction_count(ETH_ACCOUNT_FROM.address),
}

# try:
#     tx = web3_manifold.eth.send_transaction(
#         params,
#     )
#     print("Request sent! Waiting for receipt")
# except ValueError as e:
#     # Skipping if TX already is added and pending
#     if "replacement transaction underpriced" in e.args[0]["message"]:
#         print("Have TX in pool we can use for the example")
#     else:
#         raise