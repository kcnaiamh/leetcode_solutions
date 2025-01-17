from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        complement_bracket = {')': '(', '}': '{', ']': '['}
        opening_bracket = list(complement_bracket.values())
        stack = deque()

        for x in s:
            if x in opening_bracket:
                stack.append(x)
                continue
            if not stack or (stack[-1] != complement_bracket[x]):
                return False
            stack.pop()
        return True if not stack else False