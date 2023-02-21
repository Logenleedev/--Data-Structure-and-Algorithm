# Method 1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ref = dict()

        for i in range(len(arr)):
            ref[arr[i]] = ref.get(arr[i], 0) + 1

        value_list = sorted(ref.values())

        for i in range(len(value_list) - 1):
            if value_list[i + 1] == value_list[i]:
                return False 

        return True 

# Method 2:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2001



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

# Time Comlexity: O(n)
# Space Complexity: O(2001)