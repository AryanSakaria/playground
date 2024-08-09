class Solution:
    def rob_og(self, nums):
        if len(nums) < 3:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(dp)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        return max(self.rob_og(nums[1:]), self.rob_og(nums[:-1]))
