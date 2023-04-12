class Solution:
    def clean(self, s):
        result = []


        for i in range(len(s)):
            # which means the char is a word
            if s[i].isalpha() == True: 
            
                result.append(s[i].lower())
            if s[i].isnumeric() == True:
                result.append(s[i])

            # char is not a word
            # do nothing -> continue the loop
        return "".join(result)

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True 
        
        cleaned_s = self.clean(s)

        left = 0
        right = len(cleaned_s) - 1


        while left <= right:
            if cleaned_s[left] != cleaned_s[right]:
                return False 

            left += 1
            right -= 1 
        return True 


# Time Complexity: O(n)
# Space Complexity: O(n)