## Insertion Sort
```python
def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
           
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums
```
## Bubble Sort
```python 
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```

## Insertion Sort
```python
def partition(nums, left, right):
    i = left
    j = right 
    while i < j:
        # find the first number which is smaller than pivot
        while i < j and nums[j] >= nums[left]:
            j -= 1
        # find the first number which is bigger than pivot 
        while i < j and nums[i] <= nums[left]:
            i += 1
        
        nums[i], nums[j] = nums[j], nums[i]
        
    nums[left], nums[i] = nums[i], nums[left]
    
    return i        
    
    
    
    
def quick_sort(nums, left, right):
    if left >= right:
        return 
    
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)

'''
是的，当我们以最左端元素为基准数时，必须先“从右往左”再”从左往右“。这个结论有些反直觉，我来详细剖析一下原因。

哨兵划分 partition() 的最后一步是 nums[left] 与 nums[i] 交换，完成交换后基准数左边的元素都小于等于基准数，这也就要求 交换前 nums[left] >= nums[i] 必须要成立。

假设我们先“从左往右寻找第一个比基准数小的元素”，那么如果找不到，则会在 i == j 时跳出循环，此时 nums[j] == nums[i] > nums[left]；也就是说，这种情况下执行最后一步交换就会出问题了，会把一个比基准数更大的元素交换至数组最左端，导致哨兵划分失败。而如果我们先“从右往左”，就不会发生这个问题了。
'''
    
```

## Binary Search
```python 3
def binarysearch(nums, target):
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mid = (high + low)//2

        if (nums[mid] < target):
            low = mid + 1
            

        if (nums[mid] > target):
            high = mid - 1
            

        if (nums[mid] == target):
            return mid

    return -1

```

lower bound binary search [left, right]
```python 3
class Solution:


    def binary(self, nums, target):
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2


            if nums[mid] < target:
                left = mid + 1
 
            else:
                right = mid - 1

        return left 
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binary(nums, target)    

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = self.binary(nums, target + 1)

        return [start, end - 1]
```


lower bound binary search [left, right)

```python 3
class Solution:
    def lower(self, nums, target):
        i = 0 
        j = len(nums)
        
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid 

        return i

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = self.lower(nums, target + 1) - 1
        return [start, end]
```