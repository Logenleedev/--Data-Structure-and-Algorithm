# Brute Force 
# 这个情况差一个 testcase 过不了 Time limit exceed
from collections import Counter 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 
        result = 1


        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                temp = s[i : j + 1]
                if len(''.join(set(temp))) == j - i + 1:
                    result = max(result, j - i + 1)


        return result 
 
# Sliding window 

# 模版：
```
for j in range(len(nums)):
    判断[i, j]是否满足条件
    while 不满足条件：
        i += 1 （最保守的压缩i，一旦满足条件了就退出压缩i的过程，使得滑窗尽可能的大）
    不断更新结果（注意在while外更新！）
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 

        pointer = 0
        result = 1
        for i in range(len(s)):
            temp = s[pointer : i + 1]
            # while 不满足条件
            while len(''.join(set(temp))) != i - pointer + 1:
                # 可以理解为 if have duplicate, then we need to shrink the window 
                pointer += 1
            # update 答案
            result = max(result, i - pointer + 1)

        return result 
# Time Complexity: O(n)
# Space Complexity: O(1)