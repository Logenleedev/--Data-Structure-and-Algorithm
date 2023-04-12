class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow pointer 
        pointer = 0

        # i is fast pointer 
        for i in range(len(nums)):
            # if find non-duplicate element
            if nums[pointer] != nums[i]:
                # we first move forward 
                pointer += 1
                # then swap the element 
                nums[i], nums[pointer] = nums[pointer], nums[i]

        # don't forget the + 1 at the end 
        return pointer + 1


# Time Complexity: O(n)
# Space Complexity: O(1)