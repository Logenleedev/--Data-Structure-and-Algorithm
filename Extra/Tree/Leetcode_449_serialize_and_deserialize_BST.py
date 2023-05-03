# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:


    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self.serialize_helper(root, res)
        return ",".join(res)
        

    def serialize_helper(self, root, res):
        if root == None:
            res.append("None")
            return 

        res.append(str(root.val))
        self.serialize_helper(root.left, res)
        self.serialize_helper(root.right, res)

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return 

        data = data.split(",")
        ans = self.deserialize_helper(data)
        return ans 

    def deserialize_helper(self, data):
        node_val = data.pop(0)

        if node_val == "None":
            return None 
        
        root = TreeNode(int(node_val))
        root.left = self.deserialize_helper(data)
        root.right = self.deserialize_helper(data)

        return root 

        


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans



# Time Complexity: O(n)
# Space Complexity: O(n)