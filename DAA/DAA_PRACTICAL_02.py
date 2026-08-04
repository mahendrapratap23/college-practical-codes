#linear search python code 
import time

# User input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter number to search: "))

print("List:", numbers)

start = time.time()

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        position = i
        break

end = time.time()

if found:
    print(f"{target} found at index {position}")
else:
    print(f"{target} not found")

print("Time Complexity: O(n)")
print(f"Execution Time: {end - start:.6f} seconds")

#output:
#Enter numbers separated by spaces: 10 20 30 40 50 60 
#Enter number to search: 40
#List: [10, 20, 30, 40, 50, 60]
#40 found at index 3
#ime Complexity: O(n)
#Execution Time: 0.000016 seconds

#binary search python code 
import time

# User input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter number to search: "))

print("Original List:", numbers)

numbers.sort()

print("Sorted List:", numbers)

start = time.time()

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        found = True
        position = mid
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

end = time.time()

if found:
    print(f"{target} found at index {position}")
else:
    print(f"{target} not found")

print("Time Complexity: O(log n)")
print(f"Execution Time: {end - start:.6f} seconds")
#output:
#Enter numbers separated by spaces: 10 20 30 40 50 60 
#Enter number to search: 40
#Original List: [10, 20, 30, 40, 50, 60]
#Sorted List: [10, 20, 30, 40, 50, 60]
#40 found at index 4
#Time Complexity: O(log n)
#Execution Time: 0.0000010 seconds