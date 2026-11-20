def longest_increasing_subsequence(nums):
    # returns the actual subsequence, not just its length
    if not nums:
        return []

    n = len(nums)
    # length[i] = length of the best subsequence ending at i
    length = [1] * n
    # prev[i] = index before i in that subsequence, -1 means start
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                prev[i] = j

    # find where the longest one ends
    end = 0
    for i in range(1, n):
        if length[i] > length[end]:
            end = i

    # walk backwards to rebuild it
    result = []
    while end != -1:
        result.append(nums[end])
        end = prev[end]
    result.reverse()
    return result


def lis_length(nums):
    # length only, no reconstruction
    return len(longest_increasing_subsequence(nums))


print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
print(longest_increasing_subsequence([7, 7, 7, 7, 7]))
print(longest_increasing_subsequence([]))
print(lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
