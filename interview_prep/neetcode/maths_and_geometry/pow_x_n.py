class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        ans = 1
        while n != 0:
            if n%2 != 0:
                ans = ans * x
            n = n >> 1
            x = x*x
        return ans