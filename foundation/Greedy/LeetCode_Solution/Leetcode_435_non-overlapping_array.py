class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Try to overlap as many as possible
        
        intervals.sort(key = lambda x: x[0])


        # count the number of non-overlapping intervals
        count = 1


        for i in range(1, len(intervals)):
            # non-overlap 
            # notice >=. For this question, [1,2] and [2, 3] are defined
            # to be non-overlapping
            if intervals[i][0] >= intervals[i - 1][1]:
                count += 1
            # overlap
            else:
                
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])

        return len(intervals) - count 
        
# Time Complexity: O(nlog(n))
# Space Complexity: O(1)