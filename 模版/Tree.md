## Tree 


搜索一条边的写法：
```python 
if (递归函数(root.left)) return ;
if (递归函数(root.right)) return ;

```
搜索整个二叉树的写法：
```python 
left = 递归函数(root.left);
right = 递归函数(root.right);
left与right的逻辑处理;
```

### Recursion - preorder 
```python
class Solution:
    def traverse(self, root, result):
        if root == None:
            return 
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)


    def preorderTraversal(self, root):
        result = []
        if root == None:
            return result
        
        self.traverse(root, result)
        return result
```


### Recursion - inorder
```python
class Solution:
    def traverse(self, root, result):
        if root == None:
            return 
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)


    def inorderTraversal(self, root):
        result = []
        if root == None:
            return result
        
        self.traverse(root, result)
        return result
```



### Recursion - postorder
```python 
class Solution:
    def traverse(self, root, result):
        if root == None:
            return 
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)


    def postorderTraversal(self, root):
        result = []
        if root == None:
            return result
        
        self.traverse(root, result)
        return result
```

### traversal - preorder
```python 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            # 中
            result.append(node.val)

            # 右
            if node.right:
                stack.append(node.right)

            # 左
            if node.left:
                stack.append(node.left)

        return result 
```

## traversal - inorder
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        cur = root 

        stack = []

        result = []

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        
        return result 

```


### traversal - postorder
```python 
class Solution:
    def postorderTraversal(self, root):
        if root == None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            # 中
            result.append(node.val)

            # 左
            if node.left:
                stack.append(node.left)

            # 右
            if node.right:
                stack.append(node.right)

            

        return result[::-1]
```


### 二叉树层序遍历
```python 
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        results = []

        que = deque([root])

        while que:
            size = len(que)

            result = []

            for _ in range(size):
                node = que.popleft()
                result.append(node.val)
                
                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            results.append(result)

        return results
```

## 二叉树回溯模版
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 1

    def getDepth(self, root, depth):
        self.result = max(depth, self.result)

        if root.left == None and root.right == None:
            return 

        if root.left != None:
            depth += 1
            self.getDepth(root.left, depth)
            depth -= 1
        
        if root.right != None:
            depth += 1
            self.getDepth(root.right, depth)
            depth -= 1

            

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0


        self.getDepth(root, 1)

        return self.result

```
## BST 单层逻辑
```python 3
if (root->val > key) root->left = deleteNode(root->left, key);
if (root->val < key) root->right = deleteNode(root->right, key);
return root 
```
## BST specific 模版
```python 3
class Solution:

    def __init__(self):
        self.result = float("inf")
        self.pre = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.getMinimumDifference(root.left)

        if self.pre != None and root != None: 

            differnence = abs(root.val - self.pre.val)

            self.result = min(differnence, self.result)

        self.pre = root

        self.getMinimumDifference(root.right)


        return self.result
```

