class Solution:
    def isValid(self, s: str) -> bool:
        # case 1: ([[]]
        # case 2: {()]
        # case 3: ())

        ref = {
            "{" : "}",
            "[" : "]", 
            "(" : ")"
        }

        stack = []

        for char in s:
            if char in ref.keys():
                stack.append(ref[char])
            elif len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
         
                return False 

        return True if len(stack) == 0 else False