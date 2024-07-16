class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            cur_len = len(ans)
            for i in range(cur_len):
                ans.append(ans[i] + [num])
        return ans
        