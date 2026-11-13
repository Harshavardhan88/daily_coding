# longest common subsequence
# finds the longest sequence that appears in both strings,
# in the same order but not necessarily next to each other

def lcs_length(a, b):
    n = len(a)
    m = len(b)

    # table[i][j] = lcs length of a[:i] and b[:j]
    table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n][m]


def lcs(a, b):
    n = len(a)
    m = len(b)

    table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # walk back from the bottom right corner to build the answer
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


print(lcs_length("abcde", "ace"))  # 3
print(lcs("abcde", "ace"))  # ace
print(lcs_length("aggtab", "gxtxayb"))  # 4
print(lcs("aggtab", "gxtxayb"))  # gtab
print(lcs_length("hello", "world"))  # 1
print(lcs("hello", "world"))  # o
