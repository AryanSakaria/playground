class Solution:
    def dfs(self, i, j):
        if i < 0 or i >= self.m:
            return 0
        if j < 0 or j >= self.n:
            return 0
        if self.visited[i][j]:
            return 0
        if self.grid[i][j] == 0:
            return 0
        self.visited[i][j] = True
        cur_area = 1
        cur_area += self.dfs(i+1,j)
        cur_area += self.dfs(i,j+1)
        cur_area += self.dfs(i-1,j)
        cur_area += self.dfs(i,j-1)
        return cur_area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.grid = grid
        cur_max = 0

        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.grid[i][j] == 1:
                    cur_max = max(cur_max, self.dfs(i,j))
        return cur_max
