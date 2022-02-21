import time;
import web3;
import json;

infura = "Your provider link here"
w3 = web3.Web3(web3.HTTPProvider(infura))

me = ''
priv = ''
gas_price = w3.eth.gasPrice
unix_time = int(time.time())

# python json handling lol
with open('./Router.json', 'r') as r:
    router_abi = json.load(r)
with open('./Dai.json', 'r') as d:
    dai_abi = json.load(d)
with open('./Weth.json', 'r') as w:
    weth_abi = json.load(w)
WETH_ADDRESS = "0xc778417E063141139Fce010982780140Aa0cD5Ab"
DAI_ADDRESS = "0xaD6D458402F60fD3Bd25163575031ACDce07538D"
ROUTER_ADDRESS = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
router = w3.eth.contract(address=ROUTER_ADDRESS, abi=router_abi)
dai = w3.eth.contract(address=DAI_ADDRESS, abi=dai_abi)
weth = w3.eth.contract(address=WETH_ADDRESS, abi=weth_abi)

data = router.functions.swapExactETHForTokens(
    0, 
    [WETH_ADDRESS, DAI_ADDRESS], 
    me, 
    unix_time  + 100000).buildTransaction(
        {'from': me,
         'value': w3.toWei(0.1, 'ether'),
         'gas': 500000, 
         'gasPrice': gas_price,
         'nonce': w3.eth.get_transaction_count(me)
        })

signed_tx = w3.eth.account.sign_transaction(data, private_key=priv)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Swap started, transaction hash: ", w3.toHex(tx_hash))








