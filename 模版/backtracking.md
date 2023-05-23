# 可以解决的问题
- 组合
- 排列
- 切割
- 子集
- 棋盘

## 回溯三部曲
1. 递归函数参数及返回值
2. 确定终止条件
3. 单层递归逻辑

模版

```python
递归函数
backtracking(parameters) -> 没有返回值


def backtracking(parameters):

    # 到叶子以后收集结果
    if (终止条件):
        收集结果
        return 

    # 单层搜索的逻辑
    for (集合的元素集):
        处理节点
        递归函数
        回溯 - 撤销处理节点的情况
    
# 如果有一个答案就可以 比如说解数独和word search 那么就可以采用二叉树的 
# 
# 处理节点
# if recursive_call(): 
    # return True 
# 回溯 - 撤销处理节点的情况


```



## Complexity Analysis
空间复杂度：递归深度 * 每次递归的空间复杂度
时间复杂度：递归次数 * 每次递归的时间复杂度



## 一些处理技巧
```python
## 数组
result.append(x)
backtracking()
result.pop()


## string 
result += "xxx"
backtracking()
result = result[:-1]
```