class Solution:
    def trim(self, s):
        s_list = list(s)

        ans = []

        right = len(s_list) - 1
        left = 0

        while left < right and s_list[left] == " ":
            left += 1
        
        while left < right and s_list[right] == " ":
            right -= 1
        
        s_list = s_list[left: right + 1]

        for ele in s_list:
            if ele != " ":
                ans.append(ele)
            elif ans[-1] != " ":
                ans.append(ele)
        a = "".join(ans)
        b = a.split(" ")

        return len(b[-1])


    def lengthOfLastWord(self, s: str) -> int:
        result = self.trim(s)
        return result 