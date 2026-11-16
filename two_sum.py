# two sum - find two numbers in a list that add up to a target
# uses a dict to remember numbers we have seen, so it runs in one pass

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def two_sum_all(nums, target):
    # returns every pair of indices that adds up to target
    seen = {}
    pairs = []
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            pairs.append((seen[need], i))
        seen[num] = i
    return pairs


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3], 7))
print(two_sum_all([1, 5, 3, 4, 2, 6], 7))
