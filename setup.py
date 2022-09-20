from web3 import Web3


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


def setup() : 
    print(web3.isConnected(), web3.eth.block_number)
    # print(w3.eth.getBlock('latest'))
    
def retrieve_gas():
    print(web3.eth.generate_gas_price())
    
    
def return_bytecode(account: str):
    return web3.eth.get_code(account)
    


if __name__ == '__main__':
    # setup()
    # retrieve_gas()
    print(return_bytecode(Router))
  

