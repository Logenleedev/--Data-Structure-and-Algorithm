# Time Complexity: O(n(log(n)))
# Space Complexity: O(n))


import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        pri_que = []
        for key, value in map.items():
            heapq.heappush(pri_que, (value, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k

        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

# Time Complexity: O(nlog(k))
# Space Complexity: O(n)