class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = 10e6
        ans = 0
        for price in prices:
            ans = max(ans, price - min_so_far)
            min_so_far = min(min_so_far, price)
        return ans
