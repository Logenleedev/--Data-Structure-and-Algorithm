"""
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. 
For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array 
will be located at either index 4, 5, 6, 7 or 8 in the input array.


input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import heapq

def solution(num, k):
    pri_que = []
    for i in range(k + 1):
        heapq.heappush(pri_que, num[i])
    
    pointer = 0 
    for i in range(k + 1, len(num)):
        # pointer move record
        num[pointer] = heapq.heappop(pri_que)
        pointer += 1

        # push later element in the heap
        # 有点滚动数组的意思
        heapq.heappush(pri_que, num[i])

    while pri_que:
        num[pointer] = heapq.heappop(pri_que)
        pointer += 1

    return num

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))