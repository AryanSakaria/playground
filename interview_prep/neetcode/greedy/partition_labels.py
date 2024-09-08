class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fin_pos = {}
        for i, c in enumerate(s):
            fin_pos[c] = i
        l = 0
        ans = [fin_pos[s[l]]]
        while l < len(s):
            if l > ans[-1]:
                ans.append(fin_pos[s[l]])
            elif fin_pos[s[l]] > ans[-1]:
                ans[-1] = fin_pos[s[l]]
            
            l += 1
        res = []
        prev = 0
        for part in ans:
            res.append(part - prev + 1)
            prev = part + 1
        # print(res)
        return res