# My Solution:
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        helper = 1
        flag = False 

        while time > 0:
            if flag:
                helper -= 1
                if helper == 1:
                    flag = False
                time -= 1
                continue
            
            helper += 1

            if helper == n:
                flag = True 

        
            time -= 1

        return helper 
# Time Complexity: O(time) 
# Space Complexity: O(1)

# Official Solution:
class Solution:
    def passThePillow(self, n: int, time: int) -> int:    
        time %= (2 * n - 2) 
        return time + 1 if time < n  else n - (time - (n - 1))

# Time Complexity: O(1)
# Space Complexity: O(1)

