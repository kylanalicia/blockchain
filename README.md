# Blockchain Project

# Overview
This project is a simple yet functional implementation of a blockchain using Python and FastAPI. It showcases core blockchain functionalities such as mining new blocks, retrieving the blockchain, fetching the last mined block, and validating the blockchain integrity.

# Getting Started
  # Prerequisites
Ensure you have the following installed:

* Python 3.8 or higher
* FastAPI
* Uvicorn (ASGI server)

# Project Structure
* blockchain.py: Contains the implementation of the Blockchain class.
* main.py: Contains the FastAPI server setup and endpoints.

# Usage
  # Running the Blockchain
Open your terminal.
=> Start an interactive Python session using IPython:
 ipython

=> Initialize the blockchain:
 bc = blockchain.Blockchain()

=> Mine a new block to the blockchain:
 bc.mine_block("hello world")

=>Get the entire block
bc.chain

# Running the FastAPI Server
=> Run the FastAPI server using Uvicorn:
uvicorn main:app --reload

# Access the API documentation:
=> Open your web browser and go to http://localhost:8000/docs. This interactive documentation allows you to test the endpoints directly from the browser.


# Example Workflow
* Mine a new block:

=> Open http://localhost:8000/docs in your browser.
Scroll to the POST /mine_block/ endpoint.
Click "Try it out".
Enter your data in the request body.
Click "Execute".

* Get the entire blockchain:
=> Open http://localhost:8000/docs in your browser.
Scroll to the GET /blockchain/ endpoint.
Click "Try it out".
Click "Execute".

* Get the last mined block:
=> Open http://localhost:8000/docs in your browser.
Scroll to the GET /previous_block/ endpoint.
Click "Try it out".
Click "Execute".

* Validate the blockchain:
Open http://localhost:8000/docs in your browser.
Scroll to the GET /validate/ endpoint.
Click "Try it out".
Click "Execute".

# Author & License
Authored by:
  # Alicia Kimani

  * Licensed under MIT License