from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pointer = 0
        start = 0
        valid = 0

        need, window = defaultdict(int), defaultdict(int)
        result = []

        for char in p:
            need[char] += 1

        for i in range(len(s)):
            # 加元素
            element = s[i]
            
            window[element] += 1

            # 算 valid
            if element in need.keys():
                if window[element] == need[element]:
                    valid += 1
            
            # while valid 
            while valid == len(need.keys()):
                # 算长度
                if i - pointer + 1 == len(p):
                    result.append(pointer)

                # discard 
                discard = s[pointer]

                if discard in need.keys():
                    if window[discard] == need[discard]:
                        valid -= 1
                    window[discard] -= 1
                    if window[discard] == 0:
                        del window[discard]

                pointer += 1
            
        return result 