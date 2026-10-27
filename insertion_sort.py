# insertion sort - picks each element and puts it in the right place
# in the part of the list that is already sorted

def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums


print(insertion_sort([5, 2, 9, 1, 7]))
print(insertion_sort([3, 3, 1, 8, 2]))
print(insertion_sort([]))
print(insertion_sort([10]))
