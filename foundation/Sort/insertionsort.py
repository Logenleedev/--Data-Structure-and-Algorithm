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
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
           
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums

# online version
def insertionSort(nums):
    for i in range(len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base
    

a = [3,2,1,4,5,10,6]
print(insertionSort(a))