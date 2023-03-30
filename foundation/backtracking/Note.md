排列组合问题：
- 元素 unique，元素用一次，backtracking(...., ....., i + 1)（树枝去重）
- 元素 unique，元素用多次，backtracking(...., ....., i) 
- 元素 不 unique, 元素用多次, i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0 (树层去重) 记住：先要排序！！！！



## 几种套路
- 收集叶子 vs 每个节点都收留
- 树层去重 vs 树枝去重
- base case different condition
- 在做一切事情之前 排序 vs 不排序

