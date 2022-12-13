# Time complexity O(n^2)
# Online Version
def insertionSort(seq):

    index = range(1, len(seq))
    for i in index:
        value = seq[i]

        while i > 0 and (seq[i] < seq[i - 1]):
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
    return seq


# My version
def insertionSort(nums):
    n = len(nums)

    for i in range(1, n):
    	while i > 0:
    		if nums[i] < nums[i - 1]:
    			nums[i - 1], nums[i] = nums[i], nums[i - 1]
    		i -= 1
    return nums
    

a = [3,2,1,4,5,10,6]
print(insertionSort(a))