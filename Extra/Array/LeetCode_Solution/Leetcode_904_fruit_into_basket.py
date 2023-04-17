

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        result = float("-inf")

  
        
        pointer = 0

        

        ref = dict()

        for i in range(len(fruits)):
            
            # 分类讨论
            if fruits[i] in ref:
                ref[fruits[i]] += 1
            else:
                ref[fruits[i]] = 1

            # 不符合 condition
            while len(ref.keys()) > 2:
                ref[fruits[pointer]] -= 1

                # 分类讨论
                if ref[fruits[pointer]] == 0:
                    del ref[fruits[pointer]]
                
                pointer += 1
                
            result = max(result, i - pointer + 1)

        
        return result if result != float("-inf") else 0

# Time Complexity: O(n)
# Space Complexity: O(n)


# labuladong 模版解法
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        res = defaultdict(int)

        count = 0
        pointer = 0

        for i in range(len(fruits)):
            res[fruits[i]] += 1


            while len(res.keys()) > 2:
                # update data 

                discard = fruits[pointer]    

                res[discard] -= 1

                if res[discard] == 0:
                    del res[discard]
                pointer += 1

            # record answer 
            count = max(count, i - pointer + 1)
        return count 