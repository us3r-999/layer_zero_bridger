import random

from web3 import Web3
from loguru import logger


class ContractsBase:
    def __init__(self):
        pass


class RpcBase:
    def __init__(self, rpc_list):
        self.rpc_list = rpc_list

    def get_random_rpc(self):
        try:
            return random.choice(self.rpc_list)
        except IndexError:
            logger.error("Please add at least one valid RPC for every chain, follow contracts/rpcs.json")
            exit(1)


class Token:
    def __init__(self, name: str, abi: str, address, pool_id: int):
        self.name = name
        self.address = Web3.to_checksum_address(address)
        self.abi = abi
        self.pool_id = pool_id
