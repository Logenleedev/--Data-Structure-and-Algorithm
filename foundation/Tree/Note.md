## 二叉树的递归
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



## 二叉树分类讨论 left or right 空还是不空
- Leetcode 101. Symmetric Tree
- Leetcode 617. Merge Two Binary Trees

就几个情况：
- 左空 右空
- 左不空 有空
- 左空 右不空
- 左不空 右不空
  - left.val != right.val
  - left.val == right.val
## 高度 vs 深度
- 求高度用后序
- 求深度用前序 


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
  - 后 (一般来说要用到叶子节点的信息。那么换句话说，一旦你发现题目和子树有关，那大概率要给函数设置合理的定义和返回值，在后序位置写代码了)
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
  
| 前序     | 中序 | 后序 |
| ----------- | ----------- | ----------- |
| 翻转二叉树      |        | 翻转二叉树 |
|   |        | 对称二叉树 |
| | 最大深度 |
| | 最小深度 |
| | 完全二叉树的节点个数 |
| 二叉树的所有路径 | |
| 路径总和 | |
| 合并二叉树 | |
| 验证二叉搜索树 | |
| | 二叉搜索树的最近公共祖先 | |



