class Solution:
    def jump(self, nums: List[int]) -> int:

        
        nextDist = 0
        curDist = 0
        res = 0

        for i in range(len(nums)):
            
            nextDist = max(nextDist, i + nums[i])

            # if i reach the current limit of curDist 
            if i == curDist:
                # if still didn't reach the end of the array 
                if curDist < len(nums) - 1:
                    # update and +1
                    curDist = nextDist
                    res += 1
                    # check whether you can reach to the end of the array after updating
                    if curDist >= len(nums) - 1:
                        break
                # reach to the end of the array 
                else:
                    break

        
        return res 

# Time Complexity: O(n)
# Space Complexity: O(1)
