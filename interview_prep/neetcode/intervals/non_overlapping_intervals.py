class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        cur_end, count = float("-inf"), 0
        for interval in intervals:
            if interval[0] >= cur_end:
                cur_end = interval[1]
            else:
                count += 1
        return count  
        