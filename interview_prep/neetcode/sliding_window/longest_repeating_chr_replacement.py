class Solution:
    def check_valid(self, l, r, s, k):
        max_elem = 0
        for i in self.count_dict:
            max_elem = max(max_elem, self.count_dict[i])
        len_str = r - l + 1
        return len_str - max_elem <= k
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, ans = 0, 0, 0
        self.count_dict = {}
        for i in range(26):
            self.count_dict[chr(65 + i)] = 0
        while r < len(s):
            
            self.count_dict[s[r]] += 1
            while not self.check_valid(l, r, s, k):
                self.count_dict[s[l]] -= 1
                l+=1
            ans = max(ans, r - l + 1)
            r+=1
        return ans
                
        