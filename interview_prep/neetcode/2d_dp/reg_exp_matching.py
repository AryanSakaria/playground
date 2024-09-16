class Solution:
    @cache
    def backtrack(self, i, j):
        if i >= len(self.s) and j >= len(self.p):
            return True
        if j >= len(self.p):
            return False
        
        matching = i < len(self.s) and (self.s[i] == self.p[j] or self.p[j] == '.')

        if j + 1 < len(self.p) and self.p[j+1] == "*":
            return ( self.backtrack(i, j + 2) or #dont take
                (matching and self.backtrack(i+1,j))) # take
        if matching:
            return self.backtrack(i+1, j+1)
        return False  
    def isMatch(self, s: str, p: str) -> bool:
        self.s, self.p = s, p
        return self.backtrack(0, 0)


        