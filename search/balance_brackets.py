"""
Given a string of round, curly, and square opening and closing brackets, return
whether the brackets are balanced (well-formed).
"""


def balance(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        else:
            # Check character is not unmatched
            if not stack:
                return False

            # Char is a closing bracket. Check top of stack if it matches.

            if (char == brackets['('] and stack[-1] != '(') or \
                    (char == brackets['['] and stack[-1] != '[') or \
                    (char == brackets['{'] and stack[-1] != '{'):
                return False

            stack.pop()

        return len(stack) == 0
