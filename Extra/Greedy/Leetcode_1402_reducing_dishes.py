
## Brute force
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction = sorted(satisfaction)

        max_value = max(satisfaction)

        if max_value < 0:
            return 0

        
        
        result = []
        for i in range(len(satisfaction)):
            time = 1
            total = 0

            for j in range(i, len(satisfaction)):
                total += satisfaction[j] * time
                time += 1
                result.append(total)


        return max(result)

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Optimized solution

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse = True)

        # res: record final result 
        # s: record prior satisfaction score 

        res = 0
        s = 0

        for num in satisfaction:

            # if satisfaction score is larger than 0, which means we can proceed 

            if s + num > 0:

                # prior + current num 
                res += s + num 

                # update satisfaction score 
                s += num 

            # if not, the sum is only going to be smaller and smaller. Therefore, we should stop     
            else:
                break


        return res 



# Time Complexity: O(n*log(n)) since sorted() function, by default, creates this much of complexity
# Space Complexity: O(n) created by the python API