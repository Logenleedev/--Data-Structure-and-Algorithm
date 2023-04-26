class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        total = arrivalTime + delayedTime 
        
        return total % 24
        
# Time Complexity: O(1)
# Space ComplexityL O(1)

