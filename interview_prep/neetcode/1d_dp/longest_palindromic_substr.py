class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        new_str = '*' + '*'.join([*s]) + '*'
        n = len(new_str)
        big_len = 0
        for i in range(n):
            l, r = i, i
            while l - 1 >= 0 and r + 1 <= n and new_str[l] == new_str[r]:
                if r - l + 1 > big_len:
                    big_len = r - l + 1 
                    ans = (l, r)
                l-= 1
                r+= 1
        l, r = ans
        l = l//2
        r = (r-1)//2
        # print(l, r)

        return s[l:r+1]