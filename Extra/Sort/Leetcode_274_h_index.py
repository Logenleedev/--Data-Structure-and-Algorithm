class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        res = 0 
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= len(citations) - i:
                res = max(res, len(citations) - i)

        return res 

# Time Complexity: O(n * log(n))
# Space Complexity: O(1)