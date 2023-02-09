

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