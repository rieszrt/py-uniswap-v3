import V3.Listener
from V3.config import Ropsten
import V3.Caller


'''
Listen to events using V3/Listener.py as follows:
'''
#Select Ethereum network
config = Ropsten()
#Select contract to listen to
listener = V3.Listener.UniswapV3Factory(config)
#See events with fromBlock filter.
for event in listener.PoolCreated(fromBlock=1):
    print(event)

'''
To call functions use V3/Caller.py. Most features are still incomplete.
'''
#Select Ethereum network
config = Ropsten()
#Select contract to call
V3Factory= V3.Caller.V3Factory(config)
#Call function
V3Factory.allPairs(1)
