#!/usr/bin/python3
"""
function module descr
"""


def makeChange(coins, total):
    """
    Function descrip
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum coins for each amount
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    # Fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still greater than total, return -1
    return dp[total] if dp[total] <= total else -1
