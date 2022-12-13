def insertionSort(nums):
    for i in range(len(nums)):
        base = nums[i]
        j = i
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base
    return insertionSort

a = [3, 1, 2, 4, 1, 2]
print(insertionSort(a))