class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x


        left = 1
        right = x 

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == x:
                return mid 


            elif mid ** 2 < x:
                left = mid + 1

            elif mid ** 2 > x:
                right = mid - 1
                
            print(left, " ", right)

        return right
        
solution = Solution()
solution.mySqrt(8)