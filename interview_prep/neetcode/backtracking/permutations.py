class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        prev_permutes = self.permute(nums[1:])
        for list_ in prev_permutes:
            for k in range(len(list_) + 1):
                list_temp = list_.copy()
                list_temp.insert(k, nums[0])
                ans.append(list_temp)
        return ans
        