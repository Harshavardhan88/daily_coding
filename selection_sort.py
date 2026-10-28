# selection sort - find the smallest element and put it in place, one by one

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([3, 1, 4, 1, 5, 9, 2]))
print(selection_sort([]))
