#!/usr/bin/python3
"""Change maker
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    remaining = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining > 0:
        if coin_idx >= num_coins:
            return -1
        if remaining - sorted_coins[coin_idx] >= 0:
            remaining -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
