class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        self.dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    self.dp[i%2][j+1] = 1 + self.dp[1-i%2][j]
                else:
                    self.dp[i%2][j+1] = max(self.dp[1-i%2][j+1], self.dp[i%2][j])
        return self.dp[1 - m%2][-1]
        