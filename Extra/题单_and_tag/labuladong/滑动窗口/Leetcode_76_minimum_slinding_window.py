from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # create default dict since we don't need to worry about error key error 

        need, window = defaultdict(int), defaultdict(int)

        # build the target window 
        for char in t:
            need[char] +=1

        start = 0
        pointer = 0
        length = float("inf")
        
        # valid 是一个表示窗口中元素满足 need 中字符串的个数

        valid = 0

        for i in range(len(s)):

            # put element in the window 
            window[s[i]] += 1
            
            # if the key is in target 
            if s[i] in need.keys():

                # check the number of satisfied key
                if window[s[i]] == need[s[i]]:
                    valid += 1

            # valid == len(need.keys()) means all char are satisfied
            # s 里面的字符串和 t 的字符串完全一致。注意此处是 unordered 的
            while valid == len(need.keys()):

                # calculate length of the key
                temp_length = i - pointer + 1
                
                # update the length of the key if necessary
                if temp_length < length:
                    length = temp_length
                    start = pointer


                discard = s[pointer]

                # the first condition is crucial. Otherwise need[discard] will create a key,value pair
                # in this case the value will be 0
                if discard in need:
                    if window[discard] == need[discard]:
                        valid -= 1
                    window[discard] -= 1
                    # means these key do not exist anymore 
                    if window[discard] == 0:
                        del window[discard]
                    

                pointer += 1
        
        return "" if length == float("inf") else s[start: start + length]
                




