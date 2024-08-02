class Solution:
    def addLand(self, r, c):
        if r < 0 or r >= self.m:
            return
        if c < 0 or c >= self.n:
            return
        if (r,c) in self.visit_set:
            return
        if self.grid[r][c] == -1:
            return
        self.visit_set.add((r,c))
        self.q.append((r,c))

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.m, self.n = len(grid), len(grid[0])
        self.q = deque()
        self.visit_set = set()
        self.grid = grid

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    self.q.append((i, j))
                    self.visit_set.add((i, j))
        dist = 0
        while self.q:
            n = len(self.q)
            for i in range(n):
                (r,c) = self.q.popleft()
                grid[r][c] = dist
                #add children
                self.addLand(r+1,c)
                self.addLand(r,c+1)
                self.addLand(r-1,c)
                self.addLand(r,c-1)
            
            dist += 1

        