排列组合问题：
- 元素 unique，元素用一次，backtracking(...., ....., i + 1)（树枝去重）
- 元素 unique，元素用多次，backtracking(...., ....., i) 
- 元素 不 unique, 元素用多次, i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0 (树层去重) 记住：先要排序！！！！



## 几种套路
- 收集叶子 vs 每个节点都收留
- 树层去重 vs 树枝去重
- base case different condition
- 在做一切事情之前 排序 vs 不排序


## 去重的"模版"

```python 
# 标记 i 取过。如果取过，那么就取剩下的元素。用于排序问题
for i in range(len(self.nums)):
    if self.used[i] == 1:
        continue 


# 树层去重。排序 + 树层去重
for i in (集合里面的元素):
    if i > 0 and self.nums[i] == self.nums[i - 1] and self.used[i - 1] == 0

# 树枝去重
# 去重逻辑主要是为了用过的元素不要重复用。常见于组合问题。比如 12 和 21 都是一样的。 但是要求元素是 unique 的
for i in range(startIndex, len(self.nums)):
    path.append(i)
    self.backtracking(result, path, i + 1)
    path.pop()

```


