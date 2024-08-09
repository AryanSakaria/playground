class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp_2 = 1
        n = len(s)
        if n == 1:
            return dp_2
        s_2 = int(s[:2])
        if s[1] == '0':
            if  s_2 > 26:
                dp_1 =  0
            else:
                dp_1 =  1
        else:
            if s_2 <= 26:
                dp_1 = 2
            else:
                dp_1 = 1
        
        if n == 2:
            return dp_1
        for i in range(2, len(s)):
            dp_cur = 0
            if s[i] != '0':
                dp_cur += dp_1
            s2 = int(s[i-1:i+1])
            if  s2 <= 26 and s2 >= 10:
                dp_cur += dp_2
            
            if dp_cur == 0:
                return 0

            dp_2 = dp_1
            dp_1 = dp_cur
        return dp_cur
        