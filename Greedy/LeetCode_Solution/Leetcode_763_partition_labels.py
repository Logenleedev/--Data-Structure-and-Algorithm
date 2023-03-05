class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26

        for i in range(len(s)):
            hash[ord(s[i]) - ord("a")] = i
        
        left = 0
        right = 0
        ans = []

        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord("a")])

            if right == i:
                ans.append(right - left + 1)
                left = i + 1
        return ans 


# Time Complexity: O(n)
# Space Complexity: O(26)