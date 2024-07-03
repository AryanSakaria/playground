class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for x in num_set:
            if not x-1 in num_set:
                y = x + 1
                while y in num_set:
                    y+=1
                ans = max(ans, y - x)
        return ans