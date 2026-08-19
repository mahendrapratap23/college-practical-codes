# Making Change Problem using Dynamic Programming

import time

# Function to find minimum number of coins
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# User input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

# Start time
start_time = time.time()

result = min_coins(coins, amount)

# End time
execution_time = time.time() - start_time

# Output
if result == float('inf'):
    print("Change cannot be made")
else:
    print("Minimum number of coins:", result)

print("Time Complexity: O(n × amount)")
print(f"Execution Time: {execution_time:.6f} seconds")


# Output:

# Enter coin denominations: 1 2 5
# Enter amount: 13
# Minimum number of coins: 4
# Time Complexity: O(n × amount)
# Execution Time: 0.000119 seconds