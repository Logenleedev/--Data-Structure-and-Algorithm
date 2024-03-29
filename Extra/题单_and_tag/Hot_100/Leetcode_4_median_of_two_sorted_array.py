# Brute Force 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)

        if len(arr) % 2 != 0:
            return arr[len(arr) // 2]
        
        else:
            return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2 ]) / 2
# Time Complexity: O((n + m) * log(n + m))
# Space Complexity: O(1)

