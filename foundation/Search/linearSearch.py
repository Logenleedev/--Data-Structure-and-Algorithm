
# Time Complexity: O(n)

def linearsearch(nums, target):
    for i in range(len(nums)): 
        if nums[i] == target:
            return i
    return -1

## can also use enumurate() function in python to simplify the process
def linearsearch_optmized(nums, target):
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1

a = [3,2,1,4,5,10,6]
print(linearsearch_optmized(a, 100))