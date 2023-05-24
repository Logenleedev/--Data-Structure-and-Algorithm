import heapq
from collections import deque 
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]

        heapq.heapify(maxHeap)
        que = deque()


        time = 0 

        #  if 有一个没空就可以操作
        while que or maxHeap:
            
            # 操作元素开始计时
            time += 1
            
            #  如果 maxheap 不是空的
            if maxHeap:

                # pop 出来并且 + 1
                cnt = heapq.heappop(maxHeap) + 1
                
                # 如果不是 0
                if cnt:
                    # 计算下次出现的时间 放到que里面
                    que.append([cnt, time + n])

            #  如果 que 不是空的
            if que:
                # 如果时间到了冷冻时间
                if que[0][1] == time:
                    # 放回 heap
                    heapq.heappush(maxHeap, que.popleft()[0])

        return time 

# Time Complexity: O(26)
# Space Complexity: O(n)