import datetime as _dt
import hashlib as _hashlib
import json as _json

class Blockchain:
    # Initialize the blockchain with a genesis block
    def __init__(self) -> None:
        self.chain = list()
        # Create the genesis block
        genesis_block = self._create_block(data="I am the genesis block", proof=1, previous_hash="0", index=1)
        # Add the genesis block to the chain
        self.chain.append(genesis_block)

    # Mine a new block with given data
    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()  # Get the last block in the chain
        previous_proof = previous_block["proof"]  # Get the proof of the last block
        index = len(self.chain) + 1  # Calculate the index of the new block
        proof = self._proof_of_work(previous_proof, index, data)  # Find the proof of work for the new block
        previous_hash = self._hash(block=previous_block)  # Hash the previous block
        # Create the new block
        block = self._create_block(data=data, proof=proof, previous_hash=previous_hash, index=index)
        self.chain.append(block)  # Add the new block to the chain
        return block  # Return the new block

    # Hash a block and return the cryptographic hash
    def _hash(self, block: dict) -> str:
        """
        Hash a block and return the cryptographic hash
        """
        encoded_block = _json.dumps(block, sort_keys=True).encode()  # Encode the block as a JSON string
        return _hashlib.sha256(encoded_block).hexdigest()  # Return the SHA-256 hash of the encoded block

    # Create the string to be hashed for proof of work
    def _to_digest(self, new_proof: int, previous_proof: int, index: str, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + data  # Create the string from the proof and data
        return to_digest.encode()  # Encode the string to bytes

    # Find the proof of work for a new block
    def _proof_of_work(self, previous_proof: str, index: int, data: str) -> int:
        new_proof = 1  # Initialize new proof
        check_proof = False  # Initialize proof validity flag

        # Loop until a valid proof is found
        while not check_proof:
            to_digest = self._to_digest(new_proof=new_proof, previous_proof=previous_proof, index=index, data=data)
            hash_value = _hashlib.sha256(to_digest).hexdigest()  # Calculate the hash of the proof
            if hash_value[:4] == "0000":  # Check if the hash has the required prefix
                check_proof = True  # Valid proof found
            else:
                new_proof += 1  # Increment the proof and try again

        return new_proof  # Return the valid proof

    # Get the last block in the chain
    def get_previous_block(self) -> dict:
        return self.chain[-1]

    # Create a new block
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),  # Add the current timestamp
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        return block  # Return the new block

    # Validate the blockchain
    def is_chain_valid(self) -> bool:
        current_block = self.chain[0]  # Start with the genesis block
        block_index = 1  # Start checking from the second block

        # Loop through all the blocks in the chain
        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            # Check if the previous hash of the current block matches the hash of the previous block
            if next_block["previous_hash"] != self._hash(current_block):
                return False

            current_proof = current_block["proof"]
            next_index, next_data, next_proof = (
                next_block["index"], 
                next_block["data"],
                next_block["proof"],
            )
            hash_value = _hashlib.sha256(
                self._to_digest(
                    new_proof=next_proof,
                    previous_proof=current_proof,
                    index=next_index,
                    data=next_data,
                )
            ).hexdigest()

            # Check if the proof of work is valid
            if hash_value[:4] != "0000":
                return False
            
            current_block = next_block  # Move to the next block
            block_index += 1

        return True  # All blocks are valid
