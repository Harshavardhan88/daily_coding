# 0/1 knapsack - pick items to maximise value without
# going over the weight limit. each item can be taken
# at most once.

def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = best value using first i items with limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                skip = dp[i - 1][w]
                dp[i][w] = max(take, skip)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_items(weights, values, capacity):
    # same as knapsack, but also returns which items were picked
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                skip = dp[i - 1][w]
                dp[i][w] = max(take, skip)
            else:
                dp[i][w] = dp[i - 1][w]

    picked = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            picked.append(i - 1)
            w -= weights[i - 1]

    picked.reverse()
    return dp[n][capacity], picked


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print(knapsack(weights, values, capacity))  # 7
print(knapsack_items(weights, values, capacity))  # (7, [0, 1])

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(knapsack(weights, values, 7))  # 9
print(knapsack(weights, values, 0))  # 0
print(knapsack([10], [100], 5))  # 0, item too heavy
