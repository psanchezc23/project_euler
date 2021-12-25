import time

import numpy as np


def exercise_031(coins_sum):
    """
    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?

    :param coins_sum: Sum of coins to reach
    :type coins_sum: int

    :return: Number of ways to reach the coins sum
    :rtype: int
    """

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = np.zeros(coins_sum + 1, dtype=np.int)
    ways[0] = 1
    for coin in coins[1:]:
        for amount in range(coin, coins_sum + 1):
            ways[amount] += ways[amount - coin]
    return sum(ways)


if __name__ == '__main__':
    start_time = time.time()
    coins_sum = 200
    print(exercise_031(coins_sum))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
