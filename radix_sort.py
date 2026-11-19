# radix sort - sorts numbers digit by digit, starting from the last digit.
# uses counting sort as a helper for each digit place, so it stays stable.
# good for ints with a fixed number of digits, runs in linear time.

def counting_sort_by_digit(nums, place):
    n = len(nums)
    output = [0] * n
    count = [0] * 10

    for num in nums:
        digit = (num // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    # go backwards so equal digits keep their order
    for i in range(n - 1, -1, -1):
        digit = (nums[i] // place) % 10
        output[count[digit] - 1] = nums[i]
        count[digit] -= 1

    for i in range(n):
        nums[i] = output[i]


def radix_sort(nums):
    if not nums:
        return nums

    max_num = max(nums)
    place = 1
    while max_num // place > 0:
        counting_sort_by_digit(nums, place)
        place *= 10
    return nums


nums = [170, 45, 75, 90, 802, 24, 2, 66]
print("before:", nums)
print("after:", radix_sort(nums[:]))

print(radix_sort([329, 457, 657, 839, 436, 720, 355]))
print(radix_sort([5, 4, 3, 2, 1]))
print(radix_sort([1000, 100, 10, 1]))
print(radix_sort([]))
