class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = list(sorted(intervals))
        stack = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= stack[-1][1]:
                stack[-1][1] = max(interval[1],stack[-1][1])
            else:
                stack.append(interval)
        return stack

        