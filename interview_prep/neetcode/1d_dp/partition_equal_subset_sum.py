class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        total_sum = sum(nums)
        if total_sum%2:
            return False
        
        subset_sum = total_sum //2
        dp = set()
        dp.add(0)

        for num in sorted(nums):
            nextDp = dp.copy()
            for t in dp:
                if num + t == subset_sum:
                    return True
                if num + t > subset_sum or num + t in nextDp:
                    continue
                nextDp.add(num + t)
            dp = nextDp

        return subset_sum in dp
                