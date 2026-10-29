# merge sort - split the list in half, sort each half, then merge them

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # one side may still have items left
    result += left[i:]
    result += right[j:]
    return result


print(merge_sort([5, 2, 9, 1, 7, 3]))
print(merge_sort([10, -1, 4, 4, 0]))
print(merge_sort([]))
print(merge_sort([42]))
