import V3.Listener
from V3.config import Ropsten
import V3.Caller
import time

'''
Listen to events using V3/Listener.py as follows:
'''
# #Select Ethereum network
# config = Ropsten()
# #Select contract to listen to
# listener = V3.Listener.UniswapV3Factory(config)
# #See events with fromBlock filter.
# for event in listener.PoolCreated(fromBlock=1):
#     print(event)

'''
To call functions use V3/Caller.py. 
'''
# Select Ethereum network
config = Ropsten()
# Select contract to call
# Caller = V3.Caller.NonfungiblePositionManager(config)
Caller = V3.Caller.V3Factory(config)
# Call function
# Caller.decreaseLiquidity(tokenId=1, liquidity=1000000, amount0Min=1000000, amount1Min = 1000000, deadline=int(time.time()))
# tx = Caller.collect(1,config.wallet["address"],100000,100000)
#https://ropsten.etherscan.io/address/0x722dd3f80bac40c951b51bdd28dd19d435762180#code
tx = Caller.createPool("0x722dd3F80BAC40c951b51BdD28Dd19d435762180","0xc778417E063141139Fce010982780140Aa0cD5Ab",3000)
