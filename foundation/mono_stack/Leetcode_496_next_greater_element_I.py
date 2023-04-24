class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # 创建答案数组
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                # 判断 num1 是否有 nums2[stack[-1]]。如果没有这个判断会出现指针异常
                if nums2[stack[-1]] in nums1:
                    # 锁定 num1 检索的 index
                    index = nums1.index(nums2[stack[-1]])
                    # 更新答案数组
                    ans[index] = nums2[i]
                # 弹出小元素
                # 这个代码一定要放在 if 外面。否则单调栈的逻辑就不成立了
                stack.pop()
            stack.append(i)
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)