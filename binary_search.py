# binary search - finds the index of a target in a sorted list
# returns -1 if the target is not there

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# quick check
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(nums, 23))  # 5
print(binary_search(nums, 2))   # 0
print(binary_search(nums, 91))  # 9
print(binary_search(nums, 100)) # -1
