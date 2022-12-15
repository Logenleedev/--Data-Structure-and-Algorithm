# Method 1: Loop through the string 

class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i] != " ":
                ans += s[i]
            else:
                ans += "%20"
        return ans

# Method 2: Brute Force using Python API
class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = "%20".join(s.split(" "))
        return ans

# Method 3: Double Pointer 
class Solution:
    def replaceSpace(self, s: str) -> str:
        space = s.count(" ")
        ans = list(s)

        ans.extend([0] * space * 2)

        left = len(list(s)) - 1
        right = len(ans) - 1

        while left >=0:
            if ans[left] == " ":
                ans[right] = "0"
                ans[right - 1] = "2"
                ans[right - 2] = "%"
                right -= 3

            else:
                ans[right] = ans[left]
                right -= 1
            left -= 1
        
        return ''.join(ans)

