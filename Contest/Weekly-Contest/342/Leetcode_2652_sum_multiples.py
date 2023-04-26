class Solution:
    def divisible(self, n):
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            return True 
        return False 
    
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        
        for i in range(1, n + 1):
            if self.divisible(i):
                total += i 
                
        return total 
        