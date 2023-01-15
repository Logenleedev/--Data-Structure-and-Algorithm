# Method 1: Brute Force
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            index = (i + 1) % len(gas)

            while index != i and rest > 0:

                rest = rest - cost[index] + gas[index]
                index = (index + 1) % len(gas)

            if rest >= 0 and index == i:
                return i 
        
        return -1 

# Method 2: Greedy

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_sum = 0
        cur_sum = 0
        start = 0


        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]


            if cur_sum < 0:
                cur_sum = 0
                start = i + 1
            
        if total_sum < 0: 
            return -1
        return start 

                