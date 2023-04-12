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



## 解题技巧
- 带着下标排序 (见[双周赛](https://github.com/Logenleedev/--Data-Structure-and-Algorithm/blob/master/Contest/Bi-Weekly-Contest/100/Leetcode_6351_find_score.py))

- 快慢指针 (python 里面一个 for 循环就完事了)
  - 快指针一般都是在前面开路
  - 慢指针负责记录/辅助