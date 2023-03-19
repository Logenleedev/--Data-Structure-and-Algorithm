def partition(nums, left, right):
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i] 
    nums[left], nums[i] = nums[i], nums[left]
    return i

def quick_sort(nums, left, right):
    if left >= right:
        return 
    pivot = partition(nums, left, right)
    print(pivot)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


a = [3, 1, 2, 4, 6]
# print(partition(a, 0, len(a) - 1))
quick_sort(a, 0, 4)
print(a)