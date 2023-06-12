'''
思路：
直接 brute force 检查就可以了。没有什么难度
'''

class Solution:
    def reverse(self, x: int) -> int:
   
        if x < 0:
            temp = list(str(x)[1:])
            temp[:] = temp[::-1]
            ans = int(''.join(temp)) * -1 
            if ans < -2 ** 31:
                return 0 
            return ans 
        else:
            temp = str(x)[::-1]
            ans = int(temp)
            if ans > 2 ** 31 - 1:
                return 0 
            return ans

# Time Complexity: O(n)
# Space Complexity: O(1)