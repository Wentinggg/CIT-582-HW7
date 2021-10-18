from web3 import Web3
from hexbytes import HexBytes

'''
The transaction fees are calculated as the amount of gas multiplied by the gas price.
'''

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
# #     This line will mess with our autograders, but might be useful when debugging
# #     print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = w3.eth.get_transaction(tx)
#     print('tx: ' + str(tx))
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    gas_price = get_transaction(tx)["gasPrice"] #YOUR CODE HERE
    return gas_price

def get_gas(tx):
    gas = w3.eth.get_transaction_receipt(tx)["gasUsed"] #YOUR CODE HERE
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx)  #YOUR CODE HERE
    print("Cost: " + str(get_gas_price(0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578) * get_gas(0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578)))
    return tx_cost

def get_block_cost(block_num):
    transactionArray = w3.eth.get_block(block_num)["transactions"]
    block_cost = 0
    for tx in transactionArray:
#         print("tx = " + str(tx))
        block_cost += get_transaction_cost(tx)
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    transactionArray = w3.eth.get_block(block_num)["transactions"]
    max_cost = 0
    for tx in transactionArray:
#         print("tx = " + str(tx))
        if max_cost < get_transaction_cost(tx):
            max_tx = tx
            max_cost = get_transaction_cost(tx)
    max_tx = HexBytes(max_tx)  #YOUR CODE HERE
    return max_tx
