from web3 import Web3
import json
from abc import ABC


class Caller(ABC):
    def getContract(self, contractJsonPath, contractAddress):
        """
        returns web3 contract object.
        :param contractJsonPath: path to json abi of contract
        :param contractAddress: address of contract
        :return:
        """
        with open(contractJsonPath, "r") as f:
            contractJson = json.loads(f.read())
        contract = self.w3.eth.contract(
            abi=contractJson["abi"],
            address=contractAddress
        )
        return contract

    def transaction(self, tx, private_key):
        """
        Sends the function call as a transaction.
        :param tx: a transaction built using the buildTransaction method
        :param private_key: Private key of wallet with Eth
        :return: Hash of the transaction sent asynchronously.
        """
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash


class V3Factory(Caller):
    def __init__(self, config):
        """
        :param config: any object from config.py
        """
        self.config = config
        self.wallet = config.wallet
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(config.contracts["V3Factory"]["abi"],
                                         config.contracts["V3Factory"]["address"]
                                         )
        print('Web3 connection successful: ', self.w3.isConnected())

    def setOwner(self, address):
        """
        Returns the total number of pairs created through the factory so far.
        """
        return self.contract.functions.setOwner(address=address).call()

    def createPool(self, token1, token2, fee):
        '''
        Creates a pool for token 1 and token 2.
        :param token1: address of first token we're sending
        :param token2: address of second token we're sending
        :return: Hash of function call.
        '''
        tx = self.contract.functions.createPair(token1, token2, fee).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.address)})
        tx_hash = self.transaction(tx, self.private_key)
        return tx_hash


class NonfungiblePositionManager(Caller):
    def __init__(self, config):
        self.config = config
        self.wallet = config.wallet
        self.w3 = Web3(Web3.HTTPProvider(config.deploy_to))
        self.contract = self.getContract(config.contracts["nonfungiblePositionManager"]["abi"],
                                         config.contracts["nonfungiblePositionManager"]["address"]
                                         )
        print('Web3 connection successful: ', self.w3.isConnected())

    def increaseLiquidity(self, tokenId, amount0Desired, amount1Desired, amount0Min, amount1Min, deadline):
        '''
        Increases the amount of liquidity in a position, with tokens paid by the msg.sender
        :param tokenId:
        :param amount0Desired:
        :param amount1Desired:
        :param amount0Min:
        :param amount1Min:
        :param deadline:
        :return:
        '''
        params = [tokenId, amount0Desired, amount1Desired, amount0Min, amount1Min, deadline]
        tx = self.contract.functions.IncreaseLiquidity(params).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.wallet['address'])})
        tx_hash = self.transaction(tx, self.wallet['privateKey'])
        return tx_hash

    def decreaseLiquidity(self, tokenId, liquidity, amount0Min, deadline):
        '''
        Decreases the amount of liquidity in a position and accounts it to the position

        :param tokenId:
        :param liquidity:
        :param amount0Min:
        :param deadline:
        :return:
        '''
        params = [tokenId, liquidity, amount0Min, deadline]
        tx = self.contract.functions.DecreaseLiquidity(params).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.wallet['address'])})
        tx_hash = self.transaction(tx, self.wallet['privateKey'])
        return tx_hash

    def collect(self, tokenId, recipient, amount0Max, amount1Max):
        '''
        Collects up to a maximum amount of fees owed to a specific position to the recipient

        :param tokenId:
        :param recipient:
        :param amount0Max:
        :param amount1Max:
        :return:
        '''
        params = [tokenId, recipient, amount0Max, amount1Max]
        tx = self.contract.functions.Collect(params).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.wallet['address'])})
        tx_hash = self.transaction(tx, self.wallet['privateKey'])
        return tx_hash

    def mint(self, token0, token1, fee, tickLower, tickUpper, amount0Desired, amount1Desired, amount0Min, amount1Min,
             recipient, deadline):
        '''
        Creates a new position wrapped in a NFT
        :param token0:
        :param token1:
        :param fee:
        :param tickLower:
        :param tickUpper:
        :param amount0Desired:
        :param amount1Desired:
        :param amount0Min:
        :param amount1Min:
        :param recipient:
        :param deadline:
        :return:
        '''
        params = [token0, token1, fee, tickLower, tickUpper, amount0Desired, amount1Desired, amount0Min, amount1Min,
                  recipient, deadline]
        tx = self.contract.functions.Mint(params).buildTransaction(
            {'nonce': self.w3.eth.getTransactionCount(self.wallet['address'])})
        tx_hash = self.transaction(tx, self.wallet['privateKey'])
        return tx_hash

    def burn(self):
        '''
        Burns a token ID, which deletes it from the NFT contract. The token must have 0 liquidity and all tokens must be collected first.

        :return:
        '''
        pass
