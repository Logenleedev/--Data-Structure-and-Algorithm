# Method 1:
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n + 1):
            ans.append(bin(i)[2:].count("1"))

        return ans 

# Method 2:
class Solution:
    def countBits(self, n: int) -> List[int]:
        

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        
        return ans 

# 1 -> 1
# 10 -> 2
# 11 -> 3 
# 100 -> 4 
# 101 -> 5 