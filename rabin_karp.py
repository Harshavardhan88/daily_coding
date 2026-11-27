# rabin karp algorithm
# finds all places where a pattern occurs in a text
# uses a rolling hash so it does not compare every character every time

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0 or m > n:
        return []

    base = 256
    mod = 101

    pattern_hash = 0
    window_hash = 0
    highest_power = 1

    # hash of the first window and the pattern
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    # base^(m-1) used to drop the first char of the window
    for i in range(m - 1):
        highest_power = (highest_power * base) % mod

    matches = []

    for i in range(n - m + 1):
        # hashes match, so check the actual characters
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        # slide the window one step to the right
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * highest_power) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod

    return matches


def count_occurrences(text, pattern):
    return len(rabin_karp(text, pattern))


text = "ababcabcabababd"
pattern = "ababd"
print(rabin_karp(text, pattern))
print(count_occurrences(text, pattern))

text2 = "aaaaa"
pattern2 = "aa"
print(rabin_karp(text2, pattern2))

text3 = "hello world"
pattern3 = "bye"
print(rabin_karp(text3, pattern3))
