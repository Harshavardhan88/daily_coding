# counting sort - counts how many times each number appears,
# then writes them back out in order

def counting_sort(nums):
    if not nums:
        return []
    smallest = min(nums)
    biggest = max(nums)
    counts = [0] * (biggest - smallest + 1)
    for num in nums:
        counts[num - smallest] += 1
    result = []
    for i in range(len(counts)):
        result += [i + smallest] * counts[i]
    return result


print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
print(counting_sort([5, -2, 4, -2, 0, 3]))
print(counting_sort([]))
print(counting_sort([7]))
