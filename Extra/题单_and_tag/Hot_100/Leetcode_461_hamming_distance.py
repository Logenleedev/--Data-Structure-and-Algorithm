class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")

# Time Complexity: O(1)
# Space Complexity: O(1)