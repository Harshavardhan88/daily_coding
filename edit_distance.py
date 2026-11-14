# edit distance - smallest number of edits (insert, delete, replace)
# to turn one word into another

def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # table[i][j] = edits needed for first i chars of word1
    # and first j chars of word2
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(
                    table[i - 1][j],      # delete
                    table[i][j - 1],      # insert
                    table[i - 1][j - 1],  # replace
                )

    return table[m][n]


print(edit_distance("kitten", "sitting"))
print(edit_distance("horse", "ros"))
print(edit_distance("flaw", "lawn"))
print(edit_distance("same", "same"))
print(edit_distance("", "abc"))
