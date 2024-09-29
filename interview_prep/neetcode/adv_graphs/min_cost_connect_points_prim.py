class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        from queue import PriorityQueue
        frontier = PriorityQueue()
        visit_set = set()
        dist = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1])
        frontier.put((0,0))
        ans = 0
        while len(visit_set) != n:
            cost, v = frontier.get()
            if v in visit_set:
                continue
            ans += cost
            visit_set.add(v)
            for i in range(n):
                if i not in visit_set:
                    frontier.put((dist(points[v], points[i]), i))
        return ans
            