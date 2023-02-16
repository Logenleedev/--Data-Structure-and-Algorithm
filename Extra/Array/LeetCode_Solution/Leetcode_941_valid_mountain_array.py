class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # corner case 
        if len(arr) < 3:
            return False

        
        left = 0
        right = len(arr) - 1

        # move left 
        while left < len(arr) - 1 and arr[left + 1] > arr[left]:
            left += 1

        # move right 
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1

        return left == right and right != 0 and left != len(arr) - 1

# Time Complexity: O(n)
# Space Complexity: O(1)