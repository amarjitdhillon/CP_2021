"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""

def validParanthesis(s):

    paranthesis = {
            "{":"}",
            "(": ")",
            "[": "]"
            }

    if len(s) == 0:    # if there is no element, it means it is valid
        return True

    if len(s) == 1:   # just one element means that other brace is missing, hence invalid
        return False

    stack = []        # used to validate if the brace is right or not

    for c in s:
        if c in paranthesis.keys():     # means it is an opening brace
            stack.append(c)
        elif c in paranthesis.values(): # means it is an closing brace
            if len(stack)>0:
                expected_opening_brace = stack.pop()
            else:
                return False
            # Let's find what should be the actual opening brace
            item_list = paranthesis.items()
            for k,v in item_list:
                if v == c:
                    actual_opening_brace = k
                    break

            if expected_opening_brace != actual_opening_brace:
                return False

        else: # means that there is some unexpected char
            return False

    return True if len(stack) == 0 else False

if __name__ == '__main__':
    # s = "()[]{}"
    # s = "()[]{"
    s = "){"
    print(validParanthesis(s))