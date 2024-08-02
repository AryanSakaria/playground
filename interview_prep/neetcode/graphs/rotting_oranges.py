class Solution:
    def addOrange(self,r, c):
        if r < 0 or r >= self.m:
            return
        if c < 0 or c >= self.n:
            return
        if self.grid[r][c] == 0:
            return
        if (r,c) in self.visit_set:
            return
        self.visit_set.add((r,c))
        self.q.append((r,c))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.time_grid = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        self.visit_set = set()
        self.grid = grid
        self.q = deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    self.q.append((i,j))
                    self.visit_set.add((i,j))
        self.time_grid = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        dist = 0
        while self.q:
            n = len(self.q)
            for i in range(n):
                (r,c) = self.q.popleft()
                self.time_grid[r][c] = dist
                self.addOrange(r+1,c)
                self.addOrange(r,c+1)
                self.addOrange(r-1,c)
                self.addOrange(r,c-1)

            dist += 1

        #if all cells that have oranges are covered
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and self.time_grid[i][j] == -1:
                    return -1
        return max(0, dist - 1)