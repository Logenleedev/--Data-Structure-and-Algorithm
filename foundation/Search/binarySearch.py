
# Time Complexity: O(log(n))
# 左闭右闭
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

a = [3,2,1,4,5,10,6]
print(binarysearch(a, 10))



# 左闭右开
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 定义target在左闭右开的区间里，即：[left, right)

        while left < right:  # 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle  # target 在左区间，在[left, middle)中
            elif nums[middle] < target:
                left = middle + 1  # target 在右区间，在[middle + 1, right)中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值