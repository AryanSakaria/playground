class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = coins
        coins = list(sorted(coins))
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break 
                if dp[i - coin] != amount + 1:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
        