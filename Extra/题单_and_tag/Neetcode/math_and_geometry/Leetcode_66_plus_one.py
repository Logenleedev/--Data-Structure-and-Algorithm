# Brute force

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # most -> least
        temp = ''


        for digit in digits:
            temp += str(digit)


        num = int(temp) + 1
        ans = [int(x) for x in str(num)]

        return ans 
        

# Time Complxity: O(n)
# Space Complexity: O(n)


# Optimized solution 


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # most -> least
        n = len(digits)


        for i in range(len(digits) - 1, -1, -1):
            # add all digit plus one 
            digits[i] += 1
            digits[i] %= 10 
            
            if digits[i] != 0:
                return digits
        # Special case such as [9] or [9,9,9]
        return [1] + [0] * n

# Time Complexity: O(n)
# Space Complexity: O(1)
