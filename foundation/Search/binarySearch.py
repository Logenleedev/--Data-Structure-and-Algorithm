
# Time Complexity: O(log(n))

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