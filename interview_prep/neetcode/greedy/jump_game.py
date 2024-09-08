class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        max_reachable_index = nums[0]
        for i in range(1, len(nums)):
            if i > max_reachable_index:
                return False
            max_reachable_index = max(max_reachable_index, i + nums[i])
        return True
        