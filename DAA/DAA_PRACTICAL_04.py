import time

# Iterative method
def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# User input
n = int(input("Enter a number: "))


# Iterative method
start_time = time.time()
result_iterative = factorial_iterative(n)
iterative_time = time.time() - start_time


# Recursive method
start_time = time.time()
result_recursive = factorial_recursive(n)
recursive_time = time.time() - start_time


# Output
print("\nFactorial using Iterative Method:", result_iterative)
print("Time Complexity: O(n)")
print(f"Execution Time: {iterative_time:.6f} seconds")

print("\nFactorial using Recursive Method:", result_recursive)
print("Time Complexity: O(n)")
print(f"Execution Time: {recursive_time:.6f} seconds")


# Sample Output:
#
# Enter a number: 5
#
# Factorial using Iterative Method: 120
# Time Complexity: O(n)
# Execution Time: 0.000100 seconds
#
# Factorial using Recursive Method: 120
# Time Complexity: O(n)
# Execution Time: 0..000057 seconds