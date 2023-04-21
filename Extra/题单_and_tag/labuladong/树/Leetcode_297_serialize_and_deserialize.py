# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.sep = ','
        self.null = 'None'
        self.list = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "None"

        ans = self.serialize_helper(root)
        return ','.join(ans)
        
    def serialize_helper(self, root):
        if root == None:
            self.list.append(self.null)
            return 
        self.list.append(str(root.val))
        self.serialize_helper(root.left)
        self.serialize_helper(root.right)
        return self.list


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_split = data.split(',')
        ans_root = self.deserialize_helper(data_split)
        return ans_root     

    def deserialize_helper(self, data):
        val = data.pop(0)
        if val == 'None':
            return None
        
        root = TreeNode(int(val))
        root.left = self.deserialize_helper(data)
        root.right = self.deserialize_helper(data)
        return root 

# Time Complexity: O(n)
# Space Complexity: O(n)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))