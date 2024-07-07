import fastapi as _fastapi
import blockchain as _blockchain

# Initialize the Blockchain instance
blockchain = _blockchain.Blockchain()
# Initialize the FastAPI app
app = _fastapi.FastAPI()

# Endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    # Check if the blockchain is valid before mining a new block
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    # Mine a new block with the provided data
    block = blockchain.mine_block(data=data)
    return block

# Endpoint to return the entire blockchain
@app.get("/blockchain/")
def get_blockchain():
    # Check if the blockchain is valid before returning the chain
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    # Return the entire blockchain
    chain = blockchain.chain
    return chain

# Endpoint that returns the previous block
@app.get("/previous_block/")
def previous_block():
    # Check if the blockchain is valid before returning the previous block
    if not blockchain.is_chain_valid():
        raise _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    # Return the previous block in the chain
    return blockchain.get_previous_block()

# Endpoint to check if the blockchain is valid
@app.get("/validate/")
def is_blockchain_valid():
    # Validate the blockchain and return the result
    is_valid = blockchain.is_chain_valid()
    return {"is_valid": is_valid}
