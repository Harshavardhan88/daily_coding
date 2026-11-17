# coin change - fewest coins to make an amount, and how many ways to do it

def min_coins(coins, amount):
    # dp[i] = fewest coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


def count_ways(coins, amount):
    # ways[i] = number of ways to make amount i
    ways = [0] * (amount + 1)
    ways[0] = 1

    # outer loop over coins so order of coins doesn't matter
    for c in coins:
        for i in range(c, amount + 1):
            ways[i] += ways[i - c]

    return ways[amount]


def coins_used(coins, amount):
    # rebuild one set of coins that makes the amount with fewest coins
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    if dp[amount] == float('inf'):
        return []

    result = []
    left = amount
    while left > 0:
        for c in coins:
            if c <= left and dp[left - c] == dp[left] - 1:
                result.append(c)
                left -= c
                break
    return result


coins = [1, 5, 10, 25]
print(min_coins(coins, 36))      # 3 -> 25 + 10 + 1
print(count_ways(coins, 5))      # 2 -> 5, 1+1+1+1+1
print(coins_used(coins, 36))     # [25, 10, 1]
print(min_coins([2], 3))         # -1, can't make 3 with only 2s
print(count_ways([1, 2, 5], 5))  # 4
