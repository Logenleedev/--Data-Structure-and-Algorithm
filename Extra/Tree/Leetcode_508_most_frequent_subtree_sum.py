# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Note:

看到 subtree sum，第一步就是去想后序
用 dict 统计频率
'''

from collections import defaultdict
class Solution:
    def __init__(self):
        self.dict = defaultdict(int)

    def traverse(self, root):
        if root == None:
            return 0 

        left = self.traverse(root.left)
        right = self.traverse(root.right) 
        sum = left + right + root.val
        self.dict[sum] += 1
        return sum



    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        self.traverse(root)

        max_freq = max(self.dict.values())
        ans = []

        for key in self.dict.keys():
            if self.dict[key] == max_freq:
                ans.append(key)

        return ans 

# Time Complexity: O(n)
# Space Complexity: O(n)
