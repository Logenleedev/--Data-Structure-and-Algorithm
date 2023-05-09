## Tips
数组类的问题，尤其是二分以及单调栈。可以思考解法的时候用举例子的方式帮助自己思考。
干想是非常困难的。

## 模拟递枕头的转圈

```python 3
assume n = 4: 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1

class Solution:
    def passThePillow(self, n: int, time: int) -> int:    
        time %= (2 * n - 2) 
        return time + 1 if time < n  else n - (time - (n - 1))

```

```python 3
num = [1,2,3,4,5,6]

for i in range(10):
    print(num[i % len(num)])

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> 4
```
## 滑动窗口
最大窗口
```python 
for j in range(len(nums)):
    判断[i, j]是否满足条件

    # 判断左侧窗口是否要收缩
    while 不满足条件：
        i += 1 （最保守的压缩i，一旦满足条件了就退出压缩i的过程，使得滑窗尽可能的大）
    不断更新结果（注意在while外更新！）
```

最小窗口
```python 
for j in range(len(nums)):
    判断[i, j]是否满足条件

    # 判断左侧窗口是否要收缩
    while 满足条件：
        不断更新结果(注意在while内更新！)
        i += 1 （最大程度的压缩i，使得滑窗尽可能的小）


```

对角线模版
```python 3
# primary diagonal 

for i in range(len(mat)):
    sum += mat[i][i]

# secondary diagonal 
for j in range(len(mat) - 1, -1, -1):
    # 4 x 4 
    # (3, 0) (2, 1), (1, 2), (0, 3)
    sum += mat[j][len(mat) - 1 - j]

```


## 解题技巧
- 带着下标排序 (见[双周赛](https://github.com/Logenleedev/--Data-Structure-and-Algorithm/blob/master/Contest/Bi-Weekly-Contest/100/Leetcode_6351_find_score.py))

- 快慢指针 (python 里面一个 for 循环就完事了)
  - 快指针一般都是在前面开路
  - 慢指针负责记录/辅助

- 开头结尾边界条件
  - 开头结尾加 [0]