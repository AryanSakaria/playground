class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        return dp[-1]
        