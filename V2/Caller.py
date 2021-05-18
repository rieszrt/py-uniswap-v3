import V2.config as config
from web3 import Web3
import json
from abc import ABC


class Caller(ABC):
    def getContract(self, contractJsonPath, contractAddress):
        with open(contractJsonPath, "r") as f:
            contractJson = json.loads(f.read())
        contract = self.w3.eth.contract(
            abi=contractJson["abi"],
            address=contractAddress
        )
        return contract

    def transaction(self,tx,private_key):
        '''
        Sends the function call as a transaction.
        :param tx: a transaction built using the buildTransaction method
        :param private_key: Private key of wallet with Eth
        :return: Hash of the transaction sent asynchronously.
        '''
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

class V2Factory(Caller):
    def __init__(self,address,private_key):
        self.address = address
        self.private_key = private_key
        self.UniswapContracts = config.uniswapContracts["UniswapV2Factory"]
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(self.UniswapContracts["contractJsonPath"],
                                           self.UniswapContracts["contractAddress"]
                                           )
        print('Web3 connection successful: ',self.w3.isConnected())

    def functions(self):
        return self.contract.functions

    def allPairsLength(self):
        '''Returns the total number of pairs created through the factory so far.'''
        return self.contract.functions.allPairsLength().call()

    def setFeeTo(self):
        return self.contract.functions.setFeeTo()

    def allPairs(self,n):
        '''Returns the address of the nth pair (0-indexed) created through the factory, or address(0) (0x0000000000000000000000000000000000000000) if not enough pairs have been created yet.
        Pass 0 for the address of the first pair created, 1 for the second, etc.'''
        return self.contract.functions.allPairs(n).call()

    def createPair(self,token1,token2):
        '''
        Creates a pool for token 1 and token 2.
        :param token1: address of first token we're sending
        :param token2: address of second token we're sending
        :return: Hash of function call.
        '''
        tx = self.contract.functions.createPair(token1,token2).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.address)})
        tx_hash = self.transaction(tx,self.private_key)
        return tx_hash


class V2Router02(Caller):
    def __init__(self,address,private_key):
        self.address = address
        self.private_key = private_key
        self.UniswapContracts = config.uniswapContracts["UniswapV2Factory"]
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(self.UniswapContracts["contractJsonPath"],
                                           self.UniswapContracts["contractAddress"]
                                           )
        print('Web3 connection successful: ',self.w3.isConnected())

    def