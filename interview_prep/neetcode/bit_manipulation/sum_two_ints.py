class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        if b == 0:
            return a if a <= max_int else ~(a^mask)
        return self.getSum( (a^b)&mask, ((a&b)<<1)&mask )