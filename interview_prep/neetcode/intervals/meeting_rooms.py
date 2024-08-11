"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x:x.start)
        cur_end = -1

        for interval in intervals:
            print(interval.start, interval.end)
            if interval.start < cur_end:
                return False
            cur_end = interval.end
        return True
