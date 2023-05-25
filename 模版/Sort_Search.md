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