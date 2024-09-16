class Solution:
    def dfs(self, i, target):
        if (i, target) in self.dp:
            return self.dp[(i, target)]

        if i == len(self.nums):
            if target == 0:
                self.dp[(i, target)] = 1
                return 1
            self.dp[(i, target)] = 0
            return 0
        ans = 0
        ans += self.dfs(i+1, target + self.nums[i])
        ans += self.dfs(i+1, target - self.nums[i])
        self.dp[(i, target)] = ans

        return ans
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.dp = {}
        return self.dfs(0, target)
        