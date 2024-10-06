class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = math.pow(-2, 31)
        INT_MAX = math.pow(2, 31) - 1
        is_neg = False
        if x < 0:
            is_neg = True
            x = x * -1
        res = 0
        while x:
            res = res*10 + x%10
            x = x // 10
        if is_neg:
            res = -1 * res

        if res < INT_MIN or res > INT_MAX:
            return 0
        return res