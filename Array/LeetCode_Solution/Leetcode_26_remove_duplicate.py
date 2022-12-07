class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        fast, slow = 1, 1
        while(fast < length):

            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow