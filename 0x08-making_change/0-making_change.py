#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize the dp array with a value greater than any possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case
    
    # Update dp array for each coin
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1

# Testing the function
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

