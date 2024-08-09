class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        word_len = [len(word) for word in wordDict]
        n = len(s)
        w_n = len(word_len)
        for i in range(1, n+1):
            for j in range(w_n):
                start_idx = i - word_len[j]
                if start_idx >= 0:
                    if dp[start_idx] and  s[start_idx:i] == wordDict[j]:
                        dp[i] = True
        return dp[-1]
        