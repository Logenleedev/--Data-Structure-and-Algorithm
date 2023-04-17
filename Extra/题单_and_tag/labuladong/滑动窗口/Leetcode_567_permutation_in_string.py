from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = defaultdict(int), defaultdict(int)

        # build the target window 
        for char in t:
            need[char] +=1

        start = 0
        pointer = 0
        length = float("inf")
        valid = 0

        for i in range(len(s)):
            # 1. 加元素
            window[s[i]] += 1
            # 2. 数 valid
            if s[i] in need.keys():
                if window[s[i]] == need[s[i]]:
                    valid += 1

            # 3. while valid 
            while valid == len(need.keys()):
                # 4. 算长度/other operation
                temp_length = i - pointer + 1

                if temp_length < length:
                    length = temp_length
                    start = pointer

                # 5. discard
                discard = s[pointer]

                if discard in need:
                    if window[discard] == need[discard]:
                        valid -= 1
                    window[discard] -= 1
                    if window[discard] == 0:
                        del window[discard]
                    

                pointer += 1
        
        return "" if length == float("inf") else s[start: start + length]