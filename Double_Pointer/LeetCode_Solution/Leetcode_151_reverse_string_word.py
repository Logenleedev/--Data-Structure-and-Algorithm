class Solution:
    def trim_space(self, s):
        n = len(s)
        left = 0
        right = n-1
        
        while left <= right and s[left] == ' ':    
            left += 1
        while left <= right and s[right] == ' ':   
            right = right-1

        tmp = []
        while left <= right:                      
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':                 
                tmp.append(s[left])
            left += 1
        return tmp

    def reverse_string_list(self, string_List, left, right):
        
        while left <= right:
            string_List[left], string_List[right] = string_List[right], string_List[left]
            left += 1
            right -= 1

    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string_list(nums, start, end-1)
            start = end + 1
            end += 1
        return None



    def reverseWords(self, s: str) -> str:
        trimed_list = self.trim_space(s)
        self.reverse_string_list(trimed_list, 0, len(trimed_list) - 1)
        self.reverse_each_word(trimed_list)
        return "".join(trimed_list)

        