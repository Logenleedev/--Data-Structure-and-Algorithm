class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            target = i + 1

            if target % 3 == 0 and target % 5 == 0:
                ans.append("FizzBuzz")
            elif target % 3 == 0:
                ans.append("Fizz")
            elif target % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(target))

        return ans 


# Time Complexity: O(n)
# Space Complexity: O(n)