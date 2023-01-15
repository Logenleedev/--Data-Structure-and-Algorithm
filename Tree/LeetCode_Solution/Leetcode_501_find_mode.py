# Method 1: Brute force

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.traversal(root.left, result)
        self.traversal(root.right, result)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = []
        ans = []
        self.traversal(root, result)

        ref = dict()

        for num in result:
            ref[num] = ref.get(num, 0) + 1
        
        max_key = [key for key, value in ref.items() if value == max(ref.values())]

        return max_key

        
# Recusion 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.result = []
        self.pre = TreeNode()
        self.max_count = 0
        self.count = 0
    def traversal(self, cur):
        if cur == None:
            return 

        self.traversal(cur.left)

        if self.pre == None:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]
        
      

        self.traversal(cur.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        self.traversal(root)

        return self.result 

        