class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0
        n = len(s)
        for i in range(n):
            l,r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l,r = i, i+1
            while l >=0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        print(count)

        return count

