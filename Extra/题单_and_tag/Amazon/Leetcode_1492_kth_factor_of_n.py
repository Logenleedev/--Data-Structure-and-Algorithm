# Method 1: Brute Force

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []

        for i in range(1, n + 1):
            if n % i == 0:
                factor.append(i)

        factor = sorted(factor)

        if len(factor) < k:
            return -1 

        return factor[k - 1]
        
# Time Complexity: O(n * log(n))
# Space Complexity: O(n)

# Method 2: heap


import heapq

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []

        for i in range(1, n + 1):
            if n % i == 0:
                heapq.heappush(factor, i)



        if len(factor) < k:
            return -1 

        ans = 0

        while k > 1:
            heapq.heappop(factor)
            k -= 1

        return factor[0]

# Time Complexity: O(log(n))
# Space Complexity: O(n)

# Method 3: pure math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # c -> counter 计数用
        c = 0 

        for i in range(1, n + 1):
            if n % i == 0:
                c += 1

                if c == k:
                    return i 


        return -1
        
# Time Complexity: O(n)
# Space Complexity: O(1)