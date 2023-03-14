# 方法论


滑动窗口只要缩，所有相关元素都得变化


最小滑窗模板

```python
while j < len(nums):
    判断[i, j]是否满足条件
    while 满足条件：
        不断更新结果(注意在while内更新！)
        i += 1 （最大程度的压缩i，使得滑窗尽可能的小）
    j += 1
```

最大滑窗模板

```python
while j < len(nums):
    判断[i, j]是否满足条件
    while 不满足条件：
        i += 1 （最保守的压缩i，一旦满足条件了就退出压缩i的过程，使得滑窗尽可能的大）
    不断更新结果（注意在while外更新！）
    j += 1

```


双指针的一些思路：
```
定义两个指针：
快指针：找不符合条件的元素
慢指针：做替换并且最后+1
```



## 易错点

假设我们想 clone 一个数组。如果你这样 clone:
```
test = num
```
那么我们 change num 的时候 test 也会变。

如果我们想 change num 但是 test 不变，那么需要

```
test = num[::]
```

三种循环不变量
- []
- [)
- (]
具体看什么时候闭可以看区间有没有意义

## 解题技巧
[labuladong](https://labuladong.gitee.io/algo/di-ling-zh-bfe1b/shuang-zhi-fa4bd/)
- 双指针 （只要数组有序就一定要反映到）
  - 快慢指针
  - 左右指针 （二分）
    - 二分
    - 两数之和 II
  
  
