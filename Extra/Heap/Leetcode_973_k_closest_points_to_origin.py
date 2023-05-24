import heapq   
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []



        # 压入
        for point in points:
            x = point[0]
            y = point[1]

            dist = ((x) ** 2 + (y) ** 2) ** (1/2)
            ans.append((dist, point))

        
        heapq.heapify(ans)
        
        res = []
        
        # pop
        for _ in range(k):
            res.append(heapq.heappop(ans)[1])

        return res

# Time Complexity: O(n * log(n))
# Space Complexity: O(k)