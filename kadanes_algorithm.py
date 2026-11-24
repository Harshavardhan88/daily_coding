# kadane's algorithm - finds the largest sum of any
# continuous chunk (subarray) in a list of numbers

def max_subarray_sum(nums):
    best = nums[0]
    current = nums[0]
    for num in nums[1:]:
        # either extend the chunk we have, or start fresh here
        if current + num > num:
            current = current + num
        else:
            current = num
        if current > best:
            best = current
    return best


def max_subarray(nums):
    # same idea, but also returns the chunk itself
    best = nums[0]
    current = nums[0]
    best_start = 0
    best_end = 0
    start = 0
    for i in range(1, len(nums)):
        if current + nums[i] > nums[i]:
            current = current + nums[i]
        else:
            current = nums[i]
            start = i
        if current > best:
            best = current
            best_start = start
            best_end = i
    return best, nums[best_start:best_end + 1]


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_sum([-3, -2, -1]))
print(max_subarray_sum([5]))
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([-3, -2, -1]))
