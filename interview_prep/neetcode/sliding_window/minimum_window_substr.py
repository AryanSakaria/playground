class Solution:
    def valid(self, s_count, t_count):
        for s in t_count:
            if s_count[s] < t_count[s]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        s_count, t_count = {},{}
        found = False
        for i in range(26):
            s_count[chr(ord('a') + i)] = 0
            t_count[chr(ord('a') + i)] = 0
            s_count[chr(ord('A') + i)] = 0
            t_count[chr(ord('A') + i)] = 0
        for s_ in t:
            t_count[s_] += 1

        l = 0
        for r in range(len(s)):
            s_count[s[r]]+=1
            while self.valid(s_count, t_count):
                if not found:
                    ans = s[l:r+1]
                    found = True
                    
                else:
                    if(r - l + 1) < len(ans):
                        ans = s[l:r+1]
                s_count[s[l]] -= 1
                l+=1
        if found:
            return ans
        return ""