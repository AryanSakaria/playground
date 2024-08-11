class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        p_q = []
        intervals.sort()
        res = {}
        i = 0
        n = len(intervals)
        for q in sorted(queries):
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(p_q, (r - l + 1, r))
                i += 1

            while p_q and p_q[0][1] < q:
                heapq.heappop(p_q)
            res[q] = p_q[0][0] if p_q else -1
        return [res[q] for q in queries]
        