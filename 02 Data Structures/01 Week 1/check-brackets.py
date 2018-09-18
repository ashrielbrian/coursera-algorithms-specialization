# python3

import sys

# Algorithm that takes in a string and returns the position of the first (if any) unmatched paran/bracket: [] {} ()
# Else, returns the string 'Success'

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def isBracketsBalanced(text):
    # Uses a Stack data structure, LIFO

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            newBracket = Bracket(next, i)
            opening_brackets_stack.append(newBracket)

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                return i + 1
            topBracket = opening_brackets_stack.pop()
            if not topBracket.Match(next):
                # if the brackets do not match, return the position
                return i + 1
    if opening_brackets_stack:
        # Checks if there is still an element in the stack
        return opening_brackets_stack.pop().position + 1
    return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    print(isBracketsBalanced(text))
    