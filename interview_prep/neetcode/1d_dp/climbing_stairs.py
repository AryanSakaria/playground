class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        i_2, i_1 = 2,1
        for i in range(2,n):
            ans = i_2 + i_1
            i_1 = i_2
            i_2 = ans
        return ans
        