import math

'''
Initially, the block reward was 50 BTC, and the reward halves every 210,000 blocks. 
Thus at Block 1 there were 50 BTC in circulation. 
At Block 2, there were 100 BTC etc.

The function should take as input a block height (integer) and 
return the total number of tokens that have been mined so far (up to and including the given block). 
The returned value should be a float.
'''
def num_BTC(b):
    c = float(210000 * (2**(b-1)))
    return c


