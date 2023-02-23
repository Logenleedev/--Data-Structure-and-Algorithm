

## 二叉树的定义

```python
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right 

```

## 二叉树的种类
- 满二叉树 (full tree)
- 完全二叉树 (complete tree)
- 平衡二叉树


## 二叉树的遍历
- 递归遍历 
  - 前
    - 时间复杂度: O(n)
    - 空间复杂度: O(n)。空间复杂度和树的高度一致。如果树为链状则会导致最大的空间复杂度。否则是O(log(N))or O(h)
  - 中
    - 时间复杂度: O(n)
    - 空间复杂度: O(n)
  - 后
    - 时间复杂度: O(n)
    - 空间复杂度: O(n)
- 迭代遍历
  - 前
    - 时间复杂度: O(n)
    - 空间复杂度: O(n) 辅助栈
  - 中
    - 时间复杂度: O(n)
    - 空间复杂度: O(n)
  - 后
    - 时间复杂度: O(n)
    - 空间复杂度: O(n)
  

- 翻转二叉树
  - 前序
  - 后序
- 对称二叉树
  - 后序
- 最大深度
  - 后序
- 最小深度
  - 后序
- 完全二叉树的节点个数
  - 后序