class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        sum_end_i = nums[0]
        for num in nums[1:]:
            sum_end_i = max(num, num + sum_end_i)
            ans = max(ans, sum_end_i)
        return ans
        