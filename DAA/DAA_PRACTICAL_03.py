import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Sort the array
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

start = time.time()

heap_sort(numbers)

end = time.time()

print("Sorted list (Heap Sort):", numbers)
print("Time Complexity: O(n log n)")
print(f"Execution Time: {end - start:.6f} seconds")

# Output:
#
# Enter numbers separated by spaces: 5 7 2 1 8 4 6
#
# Original list: [5, 7, 2, 1, 8, 4, 6]
# Sorted list (Heap Sort): [1, 2, 4, 5, 6, 7, 8]
# Time Complexity: O(n log n)
# Execution Time: 0.000013 seconds