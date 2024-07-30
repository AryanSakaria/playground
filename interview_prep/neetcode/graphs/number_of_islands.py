class Solution:
    def dfs(self, i, j):
        if i >= self.m or i < 0:
            return
        if j >= self.n or j < 0:
            return
        if self.grid[i][j] == "0":
            return
        if self.visited[i][j]:
            return

        self.visited[i][j] = True
        self.dfs(i+1, j)
        self.dfs(i, j+1)
        self.dfs(i-1, j)
        self.dfs(i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.grid = grid
        self.m, self.n = m, n

        for i in range(m):
            for j in range(n):
                if not self.visited[i][j] and grid[i][j] == "1":
                   
                    count+=1
                    self.dfs(i,j)
        return count