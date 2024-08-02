class Solution:
    def dfs(self, i, j, visited):
        visited[i][j] = True
        if i + 1 > 0 and \
           i + 1 < self.m and \
           self.heights[i+1][j] >= self.heights[i][j] and \
           not visited[i+1][j]:
           self.dfs(i+1,j,visited)
        if i - 1 >= 0 and \
           i - 1 < self.m and \
           self.heights[i-1][j] >= self.heights[i][j] and \
           not visited[i-1][j]:
           self.dfs(i-1,j,visited)

        if j +1 > 0 and \
           j + 1 < self.n and \
           self.heights[i][j+1] >= self.heights[i][j] and \
           not visited[i][j+1]:
           self.dfs(i,j+1,visited)

        if j - 1 >= 0 and \
           j - 1 < self.n and \
           self.heights[i][j-1] >= self.heights[i][j] and \
           not visited[i][j-1]:
           self.dfs(i,j-1,visited)

            
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m, self.n = len(heights), len(heights[0])
        visitedAtlantic = [[False for _ in range(self.n)] for _ in range(self.m)]
        visitedPacific = [[False for _ in range(self.n)] for _ in range(self.m)]


        for i in range(self.m):
            self.dfs(i, 0, visitedPacific)
            self.dfs(i, self.n-1, visitedAtlantic)

        for j in range(self.n):
            self.dfs(0, j, visitedPacific)
            self.dfs(self.m-1, j, visitedAtlantic)


        ans = []
        for i in range(self.m):
            for j in range(self.n):
                if visitedAtlantic[i][j] and visitedPacific[i][j]:
                    ans.append([i,j])
        return ans
