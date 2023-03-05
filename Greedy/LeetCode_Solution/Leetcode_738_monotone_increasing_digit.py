class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int: 

        ans = []

        n_str = str(n)

        for num in n_str:
            ans.append(num)
        

        for i in range(len(ans) - 1, 0, -1):
            if int(ans[i - 1]) > int(ans[i]):
                ans[i:] = '9'*(len(ans) - i)
                ans[i - 1] = str(int(ans[i - 1]) - 1)
        
        result = int("".join(ans))
        return result 
        


# Time Complexity: O(n)
# Space Complexity: O(n) n is the length of the number


            