# solution
# push open brackets to the stack
# when closing bracket pop from the stac and match same type
    # if not the same type return False
# if stack empty return true

def valid_parentheses(s):
    stack = []

    map = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    openings = map.values()
    closings = map.keys()

    for c in s:
        if c in openings:
            stack.append(c)
        
        if c in closings:
            if len(stack) == 0:
                return False
            last_opening = stack.pop()
            if map[c] != last_opening:
                return False

    return len(stack) == 0

# T: O(n)
# M: O(n)


assert valid_parentheses("[]{}()")
assert valid_parentheses("[({}())]")
assert valid_parentheses("(((({}))))")
assert valid_parentheses("(((({})))") == False
assert valid_parentheses(")((({})))") == False
assert valid_parentheses("(((({[}])))") == False
