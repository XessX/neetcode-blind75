# Problem: Valid Parentheses
# Return True if every opening bracket has a correct closing bracket in order.

def isValid(s):
    stack = []
    open_to_close = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in open_to_close:
            stack.append(char)
        else:
            if not stack:
                return False
            last_open = stack.pop()
            if open_to_close[last_open] != char:
                return False

    return len(stack) == 0

# Example usage
print(isValid("({[]})"))  # Output: True
print(isValid("([)]"))    # Output: False
