class Solution:
    def decodeString(self, s: str) -> str:
        stack = []


        for i in range(len(s)):
            if s[i] == ']':

                # collect inner string between '[]', but not including '[' and ']'
                k = '' 
                while stack[-1] != '[':
                    k = stack.pop() + k 
                
                # pop '['
                stack.pop()

                # collect digit 
                f = '' 
                while len(stack) > 0 and stack[-1].isdigit() == True:
                    f = stack.pop() + f
                
                # start building the string
                k = int(f) * k

                # append back to the stack 
                stack.append(k)
            else:
                stack.append(s[i])
        return "".join(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)
 