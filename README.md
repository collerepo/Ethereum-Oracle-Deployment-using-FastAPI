# Ethereum-Oracle-Deployment-using-FastAPI
This project is intended to show how an Ethereum oracle contract is deployed using the FastAPI framework.

In order to be able to do so, the following steps must be followed:

1) Install the required libraries. You'll need the web3 and fastapi libraries to interact with the Ethereum blockchain and create the API, respectively. You can install them using 'pip':
---------------------------------
pip install web3
pip install fastapi
---------------------------------
2) Next, you'll need to import the required libraries and your oracle contract into your Python script. You can do this using the following code:
---------------------------------
from web3 import Web3
from fastapi import FastAPI
from solc import compile_source

##Read the Solidity source code
with open('contracts/Oracle.sol', 'r') as f:
    contract_source_code = f.read()

##Compile the Solidity code
compiled_sol = compile_source(contract_source_code)

##Extract the ABI and bytecode for the Oracle contract
oracle_abi = compiled_sol['<stdin>:Oracle']['abi']
oracle_bytecode = compiled_sol['<stdin>:Oracle']['bin']
---------------------------------
3) Next, you'll need to create a function to deploy the oracle contract to the Ethereum blockchain. This function should take two arguments: the 'web3' object and the 'price_feed_address', and return the address of the deployed contract. Here's an example of how you might do this:
---------------------------------
  def deploy_oracle(web3, price_feed_address):
    ##Create a contract object for the Oracle contract
    Oracle = web3.eth.contract(abi=oracle_abi, bytecode=oracle_bytecode)

    ##Get the account to use for the deployment
    account = web3.eth.accounts[0]

    ##Set the update interval (in seconds) for the price data
    update_inter
