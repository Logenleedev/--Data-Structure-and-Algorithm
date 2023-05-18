class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            # 2 ^ -2
            # |
            # v convert to 
            # (1 / 2) ^ 2

            return self.myPow(1 / x, -n)
        
        elif n == 0:
            return 1 

        elif n == 1:
            return x 

        # if n is odd:
        # x ^ n = x * (x * x) ^ (n // 2) 
        # if n is even:
        # x ^ n = (x * x) ^ (n // 2)

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

# 本质上我们对 n 进行了二分分解
# Time Complexity: O(log(n))
# Space Complexity: O(log(n))