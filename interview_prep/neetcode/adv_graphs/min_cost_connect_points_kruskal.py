class Solution:
    def find(self, v):
        if v == self.parent[v]:
            return v
        p = self.find(self.parent[v])
        self.parent[v] = p
        return p
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.size[a] < self.size[b]:
            a, b = b,a 
        self.parent[b] = a
        self.size[a] += self.size[b]
        

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
    
        nodes_added = set()
        from queue import PriorityQueue
        pq = PriorityQueue()
        n = len(points)
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        def get_dist(a, b):
            ans = abs(a[0] - b[0]) + abs(a[1]-b[1])
            return ans

        for i in range(n):
            for j in range(n):
                dist = get_dist(points[i], points[j])
                pq.put((dist, i, j))

        added_count = 0
        cost = 0
        while added_count != len(points)-1:
            e_c, a, b = pq.get()
            if self.find(a) != self.find(b):
                self.union(a, b)
                cost += e_c 
                added_count += 1
        return cost