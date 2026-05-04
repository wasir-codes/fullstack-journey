# LeetCode #20 - Valid Parentheses
# Approach: Stack - push opening brackets, match and pop on closing brackets
# Time: O(n) | Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False        
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack