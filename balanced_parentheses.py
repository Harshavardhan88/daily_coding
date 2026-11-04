def is_balanced(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


print(is_balanced("([])"))
print(is_balanced("([)]"))
print(is_balanced("{[()]}"))
print(is_balanced("((("))
print(is_balanced(""))
