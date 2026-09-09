# Implementation of Matrix Chain Multiplication using Dynamic Programming

import time

# Function to find minimum multiplication cost
def matrix_chain_order(p):
    n = len(p) - 1

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        p[i] * p[k + 1] * p[j])

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# User input
p = list(map(int, input("Enter matrix dimensions: ").split()))

# Start time
start_time = time.time()

result = matrix_chain_order(p)

# End time
execution_time = time.time() - start_time

# Output
print("Minimum number of multiplications:", result)
print("Time Complexity: O(n^3)")
print(f"Execution Time: {execution_time:.6f} seconds")


# Output:
#
# Enter matrix dimensions: 10 20 30 40 
#Minimum number of multiplications: 13000
#Time Complexity: O(n^3)
#Execution Time: 0.000123 seconds
#
# Because:
# A1 = 10 × 20
# A2 = 20 × 30
# A3 = 30 × 40
#
# Best order:
# (A1 × A2) × A3
#
# Cost:
# (10 × 20 × 30) + (10 × 30 × 40)
# = 6000 + 12000
# = 18000