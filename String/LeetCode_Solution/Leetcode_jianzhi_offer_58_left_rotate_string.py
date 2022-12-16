# Method 1: Slice

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        ans = ""
        if n >= len(s):
            return s
        else:
            
            ans += s[n:]
            ans += s[0: n]
            return ans
        
# Method 2: reverse string
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        ans = list(s)
        ans[0: n] = reversed(ans[0: n])
        ans[n:] = reversed(ans[n:])
        ans = reversed(ans)
        return "".join(ans)