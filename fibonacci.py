# fibonacci numbers: each number is the sum of the two before it
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    # simple loop version, builds the sequence one step at a time
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def fib_number(n):
    # just the nth fibonacci number (0-indexed), no list needed
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    # recursive version, easy to read but slow for big n
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci(10))
print(fib_number(10))
print(fibonacci_recursive(10))
