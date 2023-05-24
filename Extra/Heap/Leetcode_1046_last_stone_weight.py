import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        pri_que = []

        

        for stone in stones:
            heapq.heappush(pri_que, -stone)


        while len(pri_que) >= 2:
        
            weight1 = -1 * heapq.heappop(pri_que)
          
            weight2 = -1 * heapq.heappop(pri_que)
            
            # 如果石头全部粉碎也不用干什么事情了

            diff = abs(weight1 - weight2)
            
            if diff == 0:
                continue 
            else:
                heapq.heappush(pri_que, -diff)


        # 分类讨论
        return -pri_que[0] if len(pri_que) != 0 else 0 

# Time Complexity: O(n * log(n))
# Space Complexity: O(n)
            
    