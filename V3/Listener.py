from web3 import Web3
import json
from abc import ABC

class Listener(ABC):
    def getContract(self, contractJsonPath, contractAddress):
        with open(contractJsonPath, "r") as f:
            contractJson = json.loads(f.read())
        contract = self.w3.eth.contract(
            abi=contractJson["abi"],
            address=contractAddress
        )
        return contract

class NonfungiblePositionManager(Listener):
    def __init__(self,config):
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(config.contracts["nonfungiblePositionManager"]["abi"],
                                         config.contracts["nonfungiblePositionManager"]["address"]
                                        )
        print('Web3 connection successful: ',self.w3.isConnected())

    def IncreaseLiquidity(self,fromBlock = 12400000,toBlock = 12400000):
        event_filter = self.contract.events.IncreaseLiquidity.createFilter(fromBlock=fromBlock,toBlock = toBlock)
        return event_filter.get_all_entries()

    def Approval(self,fromBlock = 12400000,toBlock = 12400000):
        event_filter = self.contract.events.Approval.createFilter(fromBlock=fromBlock,toBlock = toBlock)
        return event_filter.get_all_entries()

    def ApprovalForAll(self,fromBlock = 12400000,toBlock = 12400000):
        event_filter = self.contract.events.ApprovalForAll.createFilter(fromBlock=fromBlock,toBlock = toBlock)
        return event_filter.get_all_entries()

    def Collect(self,fromBlock = 12400000,toBlock = 12400000):
        event_filter = self.contract.events.Collect.createFilter(fromBlock=fromBlock,toBlock = toBlock)
        return event_filter.get_all_entries()

    def DecreaseLiquidity(self,fromBlock = 12400000,toBlock = 12400000):
        event_filter = self.contract.events.DecreaseLiquidity.createFilter(fromBlock=fromBlock,toBlock = toBlock)
        return event_filter.get_all_entries()

class UniswapV3Factory(Listener):
    def __init__(self,config):
        self.wallet = config.wallet
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(config.contracts["V3Factory"]["abi"],
                                         config.contracts["V3Factory"]["address"]
                                        )
        print('Web3 connection successful: ',self.w3.isConnected())

    def FeeAmountEnabled(self,fromBlock = 12400000):
        event_filter = self.contract.events.OwnerChanged.createFilter(fromBlock=fromBlock)
        return event_filter.get_all_entries()

    def OwnerChanged(self,fromBlock = 12400000):
        event_filter = self.contract.events.OwnerChanged.createFilter(fromBlock=fromBlock)
        return event_filter.get_all_entries()

    def PoolCreated(self,fromBlock = 12400000):
        event_filter = self.contract.events.PoolCreated.createFilter(fromBlock=fromBlock)
        return event_filter.get_all_entries()

