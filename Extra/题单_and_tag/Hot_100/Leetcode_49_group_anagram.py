# Brute force 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = [[0 for _ in range(26)] for _ in range(len(strs))]

        # count char count

        for i in range(len(strs)):
            phrase = strs[i]
            for j in range(len(phrase)):
                word = phrase[j]
                ref[i][ord(word) - ord("a")] += 1


        res = []

        for i in range(len(strs)):
            if strs[i] == 1:
                continue
            temp = []
            temp.append(strs[i])
            for j in range(i + 1, len(strs)):
                if strs[j] == 1:
                    continue 
                if ref[i] == ref[j]:
                    temp.append(strs[j])
                    strs[j] = 1
            res.append(temp[:])

        return res 

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n ^ 2)


# Method 2: Hash
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}


        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]

        return list(dict.values())


# Time Complexity: O(n) 
# Space Complexity: O(n)