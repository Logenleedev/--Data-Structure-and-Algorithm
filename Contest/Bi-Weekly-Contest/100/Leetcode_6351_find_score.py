class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = sorted(enumerate(nums), key = lambda x: x[1])
        
        # 带着下标排序 给出一点多余地方的
        a = [False] * (len(nums) + 2)

        result = 0

        for i, item in nums:

            # 如果下标没有用过
            if a[i] == False:
                # 收到结果集合里面
                result += item 
                # Make a note 
                a[i] = True 
                a[i - 1] = True 
                a[i + 1] = True 
            
        return result 
        
# Time Complexity: O(n)
# Space Complexity: O(n)