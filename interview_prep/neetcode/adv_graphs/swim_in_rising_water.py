class Solution:
    def add_edge(self, i, j, parent):
        if i >= self.m or i < 0:
            return
        if j >= self.n or j < 0:
            return
        k = i * self.n + j 
        if k in self.visit:
            return    
        weight = max(self.grid[i][j], self.weights[parent]) 
        self.p_q.put((weight, k))
        
         
    def swimInWater(self, grid: List[List[int]]) -> int:
        from queue import PriorityQueue
        self.p_q = PriorityQueue()
        self.p_q.put((grid[0][0], 0)) # weight, node
        self.visit = set()
        self.m, self.n = len(grid), len(grid[0])
        self.weights = [-1 for _ in range(self.m * self.n)]
        self.grid = grid
        self.weights[0] = self.grid[0][0]
        while not self.p_q.empty():
            w, k = self.p_q.get()
            self.weights[k] = w
            i, j = k // self.n, k % self.n
            if i == self.m -1 and j == self.n -1:
                return w
            if  k in self.visit:
                continue
            self.visit.add(k)
            self.add_edge(i+1, j, k)
            self.add_edge(i  , j+1, k)
            self.add_edge(i-1, j, k)
            self.add_edge(i  , j-1, k)
        return self.weights[self.m*self.n - 1]