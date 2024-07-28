#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
    coins (list): A list of coin denominations.
    total (int): The target amount.
    
    Returns:
    int: Fewest number of coins needed to meet total. -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize an array to store minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
