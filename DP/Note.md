所以求组合类问题的公式，都是类似这种:
```python 3
dp[j] += dp[j - nums[i]]

# 注意dp[0]千万别弄成0.这样会使所有元素全都是0.根据情况具体分析 （一般是1）
```





## 字符串问题

Q: 最长重复子数组
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
```python 
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
```

Q: 最长公共子序列
输入：text1 = "abcde", text2 = "ace" 输出：3 解释：最长公共子序列是 "ace"，它的长度为 3。
```python 
if text1[j-1] == text2[i-1]:
    dp[i][j] = dp[i-1][j-1]+1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # 可以删除 text1 or text2 
```

Q: 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列
示例 1： 输入：s = "abc", t = "ahbgdc" 输出：true
```python 
if s[i-1] == t[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = dp[i][j-1]
    # 只能删除 t 
```

Q: 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

```python 
if s[i-1] == t[j-1]:
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # 只能删除 s
else:
    dp[i][j] = dp[i-1][j]
    # 只能删除 s
```

Q: 两个字符串的删除操作
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
```python 
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
```


Q: 编辑距离
```python 
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
```


解题步骤：
1. 先看看是否要分类讨论 A[i - 1] == B[j - 1] 和 A[i - 1] != B[j - 1]
2. 紧接着对于 A[i - 1] == B[j - 1] 分析，（一般来说都是 in the form of dp[i][j] = dp[i - 1][j - 1] .....）
3. 对于 A[i - 1] != B[j - 1]，进行分析。看看可以删除谁（一共三种情况：删A，删B， 都删除）


