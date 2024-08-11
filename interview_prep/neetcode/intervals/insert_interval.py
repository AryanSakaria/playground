class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left_list = []
        right_list = []
        l, r = newInterval[0], newInterval[1]

        for interval in intervals:
            if interval[1] < l:
                left_list.append(interval)

            elif interval[0] > r:
                right_list.append(interval)
                continue
            else:
                l,r = min(l,interval[0]), max(r,interval[1])
        
        return left_list + [[l, r]] + right_list
        