class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m

        for i in range(len(nums2)):
            nums1[pointer1] = nums2[i]
            pointer1 += 1

        nums1.sort()

# Time Complexity: O((m + n) * log(m + n))
# Space Complexity: O(1)


# two pointer
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # 相等走哪个都可以
            else:
                nums1[k] = nums2[j] 
                j -= 1

            k -= 1
        
        # if i 走完了直接放 j 就可以
        # if j 走完了不用做啥
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

# Time Complexity: O(n + m)
# Space Complexity: O(1)
