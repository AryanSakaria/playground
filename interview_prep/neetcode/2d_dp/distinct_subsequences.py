class Solution:
    def dfs(self, i, j):
        # print(s, t)
        if (i, j) in self.DP:
            return self.DP[(i,j)]
        if i >= self.m:
            return 0
        if j >= self.n:
            return 1
        len_s = self.m - i
        len_t = self.n - j
        if len_s < len_t:
            self.DP[(i,j)] = 0
            return 0
        if len_t == 0:
            return 1
        if self.s[i:] == self.t[j:]:
            self.DP[(i,j)] = 1
            return 1
        ans = 0
        
        if self.s[i] == self.t[j]:
            ans += self.dfs(i+1, j+1)
            # else:
        ans += self.dfs(i+1, j)
        self.DP[(i, j)] = ans
        return ans
        
    def numDistinct(self, s: str, t: str) -> int:
        self.m, self.n = len(s), len(t)
        self.s, self.t = s, t
        self.DP = {}
        return self.dfs(0,0)
