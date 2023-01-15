# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        
        begin = 0

        end = len(nums) - 1



        mid = ( end + begin ) // 2

        root = TreeNode(nums[mid])

        left_array = nums[begin: mid ]
        right_array = nums[mid + 1:]

        root.left = self.sortedArrayToBST(left_array)
        root.right = self.sortedArrayToBST(right_array)
        return root 

