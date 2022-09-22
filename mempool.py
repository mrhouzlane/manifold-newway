from web3 import Web3
import asyncio


addresses = [
    "0xc8A9B074684B78F2F8F44aE692e47b5674af0Efa",
    "0x016eE5b250Cb8036f1D6F444b699d6E773A6649E",
    "0xcadA750792A3Ac6aB14561124CCE195bc8240C14",
    "0xcadA750792A3Ac6aB14561124CCE195bc8240C14",
    "0xd03B582E3cF4A8e5411ADd7f8bCFc632be1C2a2E",
    "0x9390D05C0643ABC62a6680f118570a3ACAB37B26",
    "0x002Fc63155c8f241574aF7685c8A05471BD1aCFf",
    "0x38B2A90eE42153c394071a7fB6EE69792bD5F28b",
    "0x58f73fD7D530BbFB97141B8aAA79D9C60BA5583c"    
]

def fetch_balance():
    
    for address in addresses :
        balance = web3.eth.get_balance(web3.toChecksumAddress(address))
        # print(balance)
        print (f"balance of address {address}: {web3.fromWei(balance, 'ether') }")

    

Router = "0xc8A9B074684B78F2F8F44aE692e47b5674af0Efa"
Multicall =  "0x016eE5b250Cb8036f1D6F444b699d6E773A6649E"

#ERC20 Tokens : 
WETH_token = "0xcadA750792A3Ac6aB14561124CCE195bc8240C14"
WBTC_token = "0xd03B582E3cF4A8e5411ADd7f8bCFc632be1C2a2E"
MANI_token = "0x9390D05C0643ABC62a6680f118570a3ACAB37B26"

#LPs: 
WETH_WBTC_LP = "0x002Fc63155c8f241574aF7685c8A05471BD1aCFf"
WETH_MANI_LP = "0x38B2A90eE42153c394071a7fB6EE69792bD5F28b"
WBTC_MANI_LP = "0x58f73fD7D530BbFB97141B8aAA79D9C60BA5583c"


web3 = Web3(Web3.HTTPProvider("http://18.188.93.177:8545"))


#Check only txs going to Router:
RouterManifold = web3.toChecksumAddress(Router)
manifoldContract = web3.eth.contract(address = RouterManifold)

def get_balance():
    
    print(web3.clientVersion)
    
    balance_WETH_WBTC_LP = web3.eth.get_balance(web3.toChecksumAddress(WETH_WBTC_LP))
    balance_WETH_MANI_LP = web3.eth.get_balance(web3.toChecksumAddress(WETH_MANI_LP))
    balance_WBTC_MANI_LP = web3.eth.get_balance(WBTC_MANI_LP)

    print(f"Balance of WETH-WBTC LP is : {balance_WETH_WBTC_LP}")
    print(f"Balance of WETH_MANI_LP LP is : {balance_WETH_MANI_LP}")
    print(f"Balance of WBTC_MANI_LP LP is : {balance_WBTC_MANI_LP}")

    
def handle_event(event):
    # print(Web3.toJSON(event))
    try: 
        getTrans = Web3.toJSON(event).strip('"')
        # print(getTrans)
        trans = web3.eth.get_transaction(getTrans) #Look up txs 
        # receipt = web3.eth.get_transaction_receipt(getTrans) #Look up tx receipts 
        # print(receipt)
        to = trans['to']
        data = trans['input']
        if to == RouterManifold:
            print(data)
        else: print('nothing to see here')
    except Exception as e:
        print(f'error occured {e}')
    

#Specify by specific contract 
event_filter = web3.eth.filter({"address": WETH_WBTC_LP })

async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
    # options = Router
    # block_filter = w3.eth.filter('latest')
    tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                # log_loop(block_filter, 2),
                log_loop(tx_filter, 2)))
    finally:
        loop.close()

if __name__ == '__main__':
    # main()
    # get_balance()
    fetch_balance()