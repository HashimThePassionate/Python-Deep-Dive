# Binary Search Algorithm
def  binary_search(array, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return -1


arr = [4, 6, 9, 13, 14, 18, 21, 24, 38] 
target = 90

result = binary_search(arr, 0, len(arr) - 1, target)
print(f"Element found: {result}") if result != -1 else print("Element not found")