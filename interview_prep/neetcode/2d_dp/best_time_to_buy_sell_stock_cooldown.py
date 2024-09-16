class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            cooldown = dfs(i+1, canBuy)
            if canBuy:
                buy = dfs(i+1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(cooldown, buy)

            else:
                sell = dfs(i+2, True) + prices[i]
                dp[(i, canBuy)] = max(cooldown, sell)
            return dp[(i, canBuy)]
        return dfs(0, True)