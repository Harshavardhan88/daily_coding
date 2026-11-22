# kmp search - find all places a pattern appears in a text
# without re-checking characters we already matched

def build_lps(pattern):
    # lps[i] = length of the longest proper prefix of pattern[:i+1]
    # that is also a suffix of it
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    if not pattern or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    found = []
    i = 0  # index in text
    j = 0  # index in pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            found.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return found


def kmp_count(text, pattern):
    return len(kmp_search(text, pattern))


print(build_lps("aabaab"))  # [0, 1, 0, 1, 2, 3]
print(kmp_search("ababcabcabababd", "ababd"))  # [10]
print(kmp_search("aaaaa", "aa"))  # [0, 1, 2, 3]
print(kmp_search("hello world", "world"))  # [6]
print(kmp_search("abc", "xyz"))  # []
print(kmp_count("abababab", "aba"))  # 3
