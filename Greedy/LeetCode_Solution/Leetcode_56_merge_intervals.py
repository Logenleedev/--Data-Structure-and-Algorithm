class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key = lambda x: x[0])
        ans = []
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            last = ans[-1]
            if last[1] >= intervals[i][0]:      
                last[1] = max(last[1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans 