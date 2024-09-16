class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP = [0 for _ in range(amount + 1)]
        DP[0] = 1
        for coin in coins:
            for i in range(amount):
                if i + 1 - coin >= 0:
                    DP[i + 1] += DP[i + 1 - coin]
        return DP[-1]
        