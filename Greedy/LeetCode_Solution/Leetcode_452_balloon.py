class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points.sort(key = lambda x: x[0])

        # count overlap number 
        result = 1

        for i in range(1, len(points)):
            # non-overlap interval
            if points[i - 1][1] < points[i][0]:
                result += 1
            # overlap interval
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])

        return result 

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)