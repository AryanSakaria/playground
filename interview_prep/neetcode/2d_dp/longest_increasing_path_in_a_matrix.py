class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.curPath = 0
        self.curMax = 0
        m, n = len(matrix), len(matrix[0])
        DP = {}
        def dfs(i, j, parent):
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            if matrix[i][j] == '#':
                return 0
            if matrix[i][j] <= parent:
                return 0
            if (i, j) in DP:
                return DP[(i,j)]
            # print(i, j, matrix[i][j])
            curChar = matrix[i][j]
            matrix[i][j] = '#'
            a = dfs(i+1, j, curChar)
            b = dfs(i, j+1, curChar)
            c = dfs(i-1, j, curChar)
            d = dfs(i, j-1, curChar)
            # self.curMax = max(self.curPath, self.curMax)
            matrix[i][j] = curChar
            DP[(i,j)] = 1 + max(a, b, c, d)
            return DP[(i,j)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, matrix[i][j] - 1))
        return ans 