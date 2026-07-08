# problem name : Valid Parentheses
# problem link : https://leetcode.com/problems/valid-parentheses/
# Difficulty : Easy
# logic : Use a stack to keep track of opening brackets. Iterate through the string, and


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[ch]:
                    return False

        return len(stack) == 0
