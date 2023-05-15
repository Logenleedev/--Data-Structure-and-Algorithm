class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        total = intervals + [newInterval]
        total = sorted(total, key = lambda x: x[0])


        stack = []
        stack.append(total[0])


        for i in range(1, len(total)):
            if total[i][0] > stack[-1][1]:
                stack.append(total[i])
            else:
                stack[-1][1] = max(stack[-1][1], total[i][1])

        return stack

# Time Complexity: O(n * log(n))
# Space Complexity: O(n)