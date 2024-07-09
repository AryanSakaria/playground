class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_dict = {}
        l, r = -1, 0 
        ans = 0
        while r < len(s):
            if not s[r] in count_dict:
                count_dict[s[r]] = 0
            count_dict[s[r]] += 1
            while count_dict[s[r]] > 1:
                l+=1
                count_dict[s[l]] -= 1
            cur_len = r - l
            ans = max(ans, cur_len)
            r+=1
        return ans
        