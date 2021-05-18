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
#Select Ethereum network
config = Ropsten()
#Select contract to call
Caller= V3.Caller.NonfungiblePositionManager(config)
#Call function
Caller.decreaseLiquidity(tokenId=1,liquidity=1000000,amount0Min=1000000,deadline=int(time.time()))
