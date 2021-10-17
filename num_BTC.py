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
    constant = 210000
    n = float(b / constant)
    era = math.floor(b / constant)
    print('n = ' + str(n), 'era = ' + str(era))
    count = float((b - constant * era) * 50 / (2 ** era))
    i = 1

    while i <= n:
        count += float((50 / (2 ** (i-1))) * constant)
        i += 1

    return count


# print(num_BTC(525000))
