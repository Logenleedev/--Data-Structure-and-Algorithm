class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []

        # 注意 left == right 是无效区间。卡哥 binary search 视频里面说过
        while left < right:
        
            # 如果相等就记录答案并且返回（因为题目中说有且仅有一个答案）
            if numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
                return result 
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        # 本题不用加，但是对于其他题目来说如果没有找到可以返回
        # [-1, -1]

# Time Complexity: O(n)
# Space Complexity: O(2)