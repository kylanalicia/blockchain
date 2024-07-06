import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain:

    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(data="I am the genesis block", proof=1, previous_hash="0", index=1
                                           )
        self.chain.append(genesis_block)

    def mine_block(self, data:str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = None

    def _to_digest(self, new_proof: int, previous_proof: int, index: str, data: str
                   ) -> bytes:
     to_digest = str(new_proof ** 2 - previous_proof ** 2 + index)  + data

     def _proof_of_work(self, previous_proof: str, index: int, data:str) -> int:
            new_proof = 1
            check_proof = False

            while not check_proof:
                to_digest = None
            pass
       

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _create_block(self, data: str, proof: int, previous_hash: str, index:int) -> dict:
       block = {
           "index": index,
           "timestamp": str(_dt.datetime.now()),
           "data": data,
           "proof": proof,
           "previous_hash": previous_hash,
       }

       return block

       