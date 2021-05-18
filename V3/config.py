class Ropsten():
    '''
    Config for calling contracts on the Ropsten Testnet.
    '''
    def __init__(self):
        self.deploy_to = 'https://ropsten.infura.io/v3/01fd207f78e64967af6443941947b977'
        self.wallet = dict(address="0xE533133C7a4Da33f7a54CBa414d5D25ac8eE4524",
                           privateKey="41552935dbbeec3374cec6e6ba776dddc9c69425f8234612280cb4020c9bc723")
        self.contracts = dict(V3Factory={"address": "0x273Edaa13C845F605b5886Dd66C89AB497A6B17b",
                                         "abi": "@uniswap/v3-core/artifacts/contracts/UniswapV3Factory.sol/UniswapV3Factory.json"},
                              nonfungiblePositionManager={"address": "0x74e838ECf981Aaef2523aa5B666175DA319D8D31",
                                                          "abi": "@uniswap/v3-periphery/artifacts/contracts/NonfungiblePositionManager.sol/NonfungiblePositionManager.json"},
                              swapRouter={"address": "0x03782388516e94FcD4c18666303601A12Aa729Ea",
                                          "abi": "@uniswap/v3-periphery/artifacts/contracts/SwapRouter.sol/SwapRouter.json"},
                              quoter={"address": "0x2F9e608FD881861B8916257B76613Cb22EE0652c",
                                      "abi": "@uniswap/v3-periphery/artifacts/contracts/lens/Quoter.sol/Quoter.json"},
                              tickLens={"address": "0x2F9e608FD881861B8916257B76613Cb22EE0652c",
                                        "abi": "@uniswap/v3-periphery/artifacts/contracts/lens/TickLens.sol/TickLens.json"},
                              v3Migrator={"address": "0x764a2557D2af049bd026D382eEE05fBC7C5425E4",
                                          "abi": "@uniswap/v3-periphery/artifacts/contracts/V3Migrator.sol/V3Migrator.json"},
                              weth9={"address": "0xc778417E063141139Fce010982780140Aa0cD5Ab",
                                     "abi": ""},
                              multicall2={"address": "0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696",
                                          "abi": ""},
                              proxyAdmin={"address": "0x0Fb45B7E5e306fdE29602dE0a0FA2bE088d04899",
                                          "abi": ""},
                              nftDescriptorLibrary={"address": "0x8b96635D10A4034eC6E146A7c1129FCfa08A47D3",
                                                    "abi": ""},
                              nonfungibleTokenPositionDescriptor={
                                  "address": "0xEAC3e2e3098b6F2766CFB302d4106Bd8D6E38540",
                                  "abi": ""},
                              descriptorProxy={"address": "0xbf1A262dA77FE8eB37A42650E196DEFFe00Cc1C9",
                                               "abi": ""})


class Gannache():
    '''
    Config for calling contracts on the Ropsten Testnet.
    '''
    def __init__(self):
        self.deploy_to = 'HTTP://127.0.0.1:7545'
        self.wallet = dict(address="0xE533133C7a4Da33f7a54CBa414d5D25ac8eE4524",
                           privateKey="41552935dbbeec3374cec6e6ba776dddc9c69425f8234612280cb4020c9bc723")
        self.contract = dict(NonfungiblePositionManager={
            "contractJsonPath": "@uniswap/v3-periphery/artifacts/contracts/NonfungiblePositionManager.sol/NonfungiblePositionManager.json",
            "contractAddress": "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        }, UniswapV3Pool={
            "contractJsonPath": "@uniswap/v3-core/artifacts/contracts/UniswapV3Pool.sol/UniswapV3Pool.json",
            "contractAddress": ""
        }, UniswapV3Factory={
            "contractJsonPath": "@uniswap/v3-core/artifacts/contracts/UniswapV3Factory.sol/UniswapV3Factory.json",
            "contractAddress": "0x1F98431c8aD98523631AE4a59f267346ea31F984"

        })
