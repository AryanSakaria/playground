class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        og_num = nums[0]
        for num in nums[1:]:
            og_num = og_num ^ num
        return og_num
    