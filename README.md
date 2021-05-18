# Python library for Uniswap V3
For interacting with the Uniswap V3 smart contract protocols using web3.py. 
V3 folder contains Listener and Caller for listening to events and calling functions of Uniswap V3.
config.py contains options for Mainnet, Ropsten and other test nets.
Check out main.py for basic examples.

## Caller: V3Factory
### CreatePool:
Creates a pool using contract addresses and fees.
#### Errors:
1. If you try to make an existing pool. ValueError: {'code': -32000, 'message': 'already known'}

## Caller: NonfungiblePositionManager
### IncreaseLiquidity:
Increases the amount of liquidity in a position, with tokens paid by the msg.sender
#### Errors:
1. If you don't add slippage check. web3.exceptions.ContractLogicError: execution reverted: Price slippage check

## Caller: NonfungiblePositionManager
### Collect:
Collects up to a maximum amount of fees owed to a specific position to the recipient
#### Errors