# Practical 6 - 0/1 Knapsack using Dynamic Programming

import time

def knapsack(weights, values, capacity):

    n = len(weights)

    # Create table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Check each item
    for i in range(1, n + 1):

        for bag in range(1, capacity + 1):

            weight = weights[i - 1]
            value = values[i - 1]

            # If item can fit
            if weight <= bag:

                take = value + dp[i - 1][bag - weight]
                skip = dp[i - 1][bag]

                dp[i][bag] = max(take, skip)

            # If item cannot fit
            else:
                dp[i][bag] = dp[i - 1][bag]

    return dp[n][capacity]


# Input
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

# Start time
start = time.time()

answer = knapsack(weights, values, capacity)

# End time
end = time.time()

# Output
print("Maximum value:", answer)
print("Time Complexity: O(n * W)")
print(f"Execution Time: {end - start:.6f} seconds")

#Enter weights: 2 3 4 5 6
#Enter values: 3 4 5 6 7 
#Enter capacity: 5
#Maximum value: 7
#Time Complexity: O(n * W)
#Execution Time: 0.000142 seconds