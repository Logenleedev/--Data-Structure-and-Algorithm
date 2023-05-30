class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        res = 0 

        # three cases:
        # 1. stack is empty 
        # 2. s[i] is (. There is no way to match the parenthenses
        # 3. stack[-1] is (

        for i in range(len(s)):
            if len(stack) == 0 or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                # record the answer
                stack.pop()
                res = max(res, i - (stack[-1] if len(stack) != 0 else -1))
        
        # return the result 
        return res 

# Time Complexity: O(n)
# Space Complexity: O(n)