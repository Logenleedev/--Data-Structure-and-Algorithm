```python 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0 
        ans = 0 
        for i in range(len(gain)):

            res += gain[i]
            ans = max(ans, res)

        return ans
```