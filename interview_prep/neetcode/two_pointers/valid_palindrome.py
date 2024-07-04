class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalnum()]).lower()
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True