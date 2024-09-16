class Solution:
    @cache
    def dfs(self, l, r):
        if (l,r) in self.DP:
            return self.DP[(l,r)]
        if l == r:
            return self.nums[l]*self.nums[l-1]*self.nums[l+1]
        a = 0
        for i in range(l, r+1):
            a = max(
                a, 
                self.nums[i] * self.nums[l-1] * self.nums[r+1] + 
                self.dfs(l, i-1) + self.dfs(i+1, r)
            )
   
        self.DP[(l,r)] = a
        return a

    def maxCoins(self, nums: List[int]) -> int:
        self.nums = [1] + nums + [1]
        self.DP = {}
        return self.dfs(1, len(self.nums)-2)
        
        