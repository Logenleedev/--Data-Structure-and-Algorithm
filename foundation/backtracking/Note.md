排列组合问题：
- 元素 unique，元素用一次，backtracking(...., ....., i + 1)（树枝去重）
- 元素 unique，元素用多次，backtracking(...., ....., i) 
- 元素 不 unique, 元素用多次, i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0 (树层去重)