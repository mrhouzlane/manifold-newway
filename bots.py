from web3 import Web3, HTTPProvider
import time

bots = [
    # "    Manifold addresses:
  "0x1b804377e4d47fa032032f9885101943a75aaf18",
  "0x56cc8bf51243d065d72dc6f422f8a6773ad4ccea",
  "0x734e361c35431a7b71c64186cd908dabf5d0476c",
  "0xc97b59333807102472d702ae388e9722a1a68ce6",
  "0x33d7adeb52707028cc437e0a4561ca57c4d1c8a0",
  "0x740c4ccd73fae5768778f8222ef33404af73c5fc",
  "0x3824ddc0e9345783ed338c28b7632626288c1e13",
  "0xa4e0e0c59c8c9f13a49d2ad829ae02f937b2cc9c",
  "0xeb7a925b624487411be2c84f1329b586d2c4a40a",
  "0x7d49234f5fe53085823470446b134e4042139b6d",
  "0x67b59a383b6ba37ade05222027372c7532f2cba2",
  "0xf80b6ed95b70dc6469aea0a1a9f983bd3ad21640",
  "0x820a47cf9a23a3bbd4321de6760fbae4184e1935",
  "0x839B878873998F02cE2f5c6D78d1B0842e58F192" # my address : // waiting for airdrop // 
]

def main():

    manifold_uri = "http://18.188.93.177:8545/"
    w3 = Web3(HTTPProvider(manifold_uri))

    for bot in bots:
        balance = w3.eth.get_balance(w3.toChecksumAddress(bot))
        print (f"balance of bot {bot}: {w3.fromWei(balance, 'ether') }")

    # block_filter = w3.eth.filter("latest")
    # print(block_filter)
    # log_loop(block_filter, 2)


def handle_event(event):
    print(event)


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

if __name__ == '__main__':
    main()