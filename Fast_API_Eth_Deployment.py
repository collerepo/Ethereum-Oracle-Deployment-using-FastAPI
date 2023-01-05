from web3 import Web3
from fastapi import FastAPI
from solc import compile_source

# Read the Solidity source code
with open('contracts/Oracle.sol', 'r') as f:
    contract_source_code = f.read()

# Compile the Solidity code
compiled_sol = compile_source(contract_source_code)

# Extract the ABI and bytecode for the Oracle contract
oracle_abi = compiled_sol['<stdin>:Oracle']['abi']
oracle_bytecode = compiled_sol['<stdin>:Oracle']['bin']

def deploy_oracle(web3, price_feed_address):
    # Create a contract object for the Oracle contract
    Oracle = web3.eth.contract(abi=oracle_abi, bytecode=oracle_bytecode)

    # Get the account to use for the deployment
    account = web3.eth.accounts[0]

    # Set the update interval (in seconds) for the price data
    update_inter