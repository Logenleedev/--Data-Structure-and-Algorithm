class Solution:
    def traverse(self, preorder, inorder):
        if preorder == []:
            return 


        # for pre order. mid, left, right 


        # Find index 
        root_val = preorder[0]
        root = TreeNode(root_val)



        # slice list 
        idx = inorder.index(root_val)
        left_inorder = inorder[: idx]
        right_inorder = inorder[idx + 1: ]

        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[len(left_inorder) + 1: ]


        root.left = self.traverse(left_preorder, left_inorder)
        root.right = self.traverse(right_preorder, right_inorder)

        return root 

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder == None:
            return 

        inorder = sorted(preorder)
        ans = self.traverse(preorder, inorder)
        return ans 


# Time Complexity: O(n)
# Space Complexity: O(n)