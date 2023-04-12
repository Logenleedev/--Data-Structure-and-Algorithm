# Brute Force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        if len(s) == 1:
            return s

        result = ""

        for i in range(len(s) - 2, -1, -1):
            for j in range(i, len(s)):
                
                compare = ''.join(list(s[i : j + 1])[::-1])
                if s[i : j + 1] == compare:
                    if j - i + 1 > len(result):
                        result = s[i : j + 1]
           
            
        return result
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# 中心扩散法：
class Solution:
    

    def palindrom(self, s, l, r):
        while l >= 0 and r < len(s) and  s[l] == s[r]:

            # 记住 这里不能把 s[l] == s[r] 当作一个新的条件放到 while 里面 要不然就是无限循环
                l -= 1
                r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s: str) -> str:


        res = ""
        for i in range(len(s)):
            # if len(palindrome) is odd
            s1 = self.palindrom(s, i, i)
            # if len(palindrome) is even 
            s2 = self.palindrom(s, i, i + 1)


            # update 
            if len(s1) > len(res):
                res = s1
            
            # update 
            if len(s2) > len(res):
                res = s2

        return res 


# DP

# 参考 leetcode 647 
class Solution:
    

    def longestPalindrome(self, s: str) -> str:

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]



        res = ""

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
  
                        dp[i][j] = 1
                    elif j - i > 1 and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                    
                    # after updating the cell, update the answer 
                    if dp[i][j] == 1 and j - i + 1 > len(res):
                        res = s[i : j + 1]

        return res 
