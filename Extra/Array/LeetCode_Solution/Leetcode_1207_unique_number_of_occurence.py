# My method:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # we need number -> freq
        

        freq = [0] * 2001




        for i in range(len(arr)):
            freq[arr[i] + 1000] += 1

        sorted_freq = sorted(freq)

        for j in range(len(sorted_freq) - 1):
            if sorted_freq[j] == sorted_freq[j + 1] and sorted_freq[j] != 0 and sorted_freq[j+1] != 0:
                return False 

        return True 
        

# Best answer:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2001


        # number -> freq
        # freq -> occure before or not 
        
        for i in range(len(arr)):
            count[arr[i] + 1000] += 1

        freq = [False] * 1001

        # 此时我们要用 count[i] 做为 key
        for i in range(len(count)):
            if count[i] > 0:
                if freq[count[i]] == False:
                    freq[count[i]] = True
                else:
                    return False 
        
        return True 
