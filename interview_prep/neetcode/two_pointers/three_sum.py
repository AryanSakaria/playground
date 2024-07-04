class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i, j, k = 0, 0, 0
        ans = []
        for i in range(n):
            if i!=0 and nums[i-1] == nums[i]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum > 0:
                    k-=1
                elif cur_sum < 0:
                    j+=1
                else:
                    ans.append((nums[i],nums[j],nums[k]))
                    j+=1
                    while j < n and nums[j-1] == nums[j]:
                        j+=1
        return ans