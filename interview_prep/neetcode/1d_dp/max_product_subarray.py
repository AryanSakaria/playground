class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_prod = 1
        best_prod = nums[0]
        n = len(nums)
        for i in range(n):
            cur_prod = nums[i]*cur_prod
            best_prod = max(best_prod, cur_prod)
            if cur_prod == 0:
                cur_prod = 1
        cur_prod = 1
        for i in range(n):
            cur_prod = nums[n - i - 1] * cur_prod
            best_prod = max(best_prod, cur_prod)
            if cur_prod == 0:
                cur_prod = 1
        return best_prod
        