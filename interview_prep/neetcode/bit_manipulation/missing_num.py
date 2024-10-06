class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_var = len(nums)
        for i in range(len(nums)):
            xor_var ^= (i^nums[i])
        return xor_var