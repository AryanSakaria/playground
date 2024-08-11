"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        num_rooms, count = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
                num_rooms = max(num_rooms, count)
            else:
                e += 1
                count -= 1
        return num_rooms

        