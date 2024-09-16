class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            DP[i][-1] = len(word1) - i
        for j in range(n):
            DP[-1][j] = len(word2) - j

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    DP[i][j] = DP[i+1][j+1]
                else:
                    DP[i][j] = 1 + min(
                        DP[i+1][j],
                        DP[i][j+1],
                        DP[i+1][j+1]
                    )
        return DP[0][0]

        