def shell_sort(nums):
    n = len(nums)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2

    return nums


def shell_sort_desc(nums):
    nums = nums[:]
    n = len(nums)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] < temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2

    return nums


print(shell_sort([12, 34, 54, 2, 3]))
print(shell_sort([5, 4, 3, 2, 1]))
print(shell_sort([1]))
print(shell_sort([]))
print(shell_sort_desc([12, 34, 54, 2, 3]))
