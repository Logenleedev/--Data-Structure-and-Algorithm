class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        ref_list = list(s)

        if len(ref_list) == 0:
            return ""
        
        for s in ref_list:
            if len(ans) != 0 and s == ans[-1]:
                ans.pop()
            else:
                ans.append(s)
        return "".join(ans)
