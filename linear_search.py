def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


nums = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(nums, 22))
print(linear_search(nums, 90))
print(linear_search(nums, 100))
print(linear_search([], 5))
print(linear_search(["apple", "banana", "mango"], "banana"))
