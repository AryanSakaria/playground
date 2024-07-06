class Solution:
    def helper(self,s, n_open, n_close, total_n, ans):
        if n_open > total_n:
            return
        if n_close > n_open:
            return
        if n_close <= n_open:
            if n_close == total_n:
                ans.append(s)
                return
            self.helper(s + '(', n_open+1, n_close, total_n, ans)
            self.helper(s + ')', n_open, n_close+1, total_n, ans)
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper('', 0, 0, n, ans)
        return ans
        
        