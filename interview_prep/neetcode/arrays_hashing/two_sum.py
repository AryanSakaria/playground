class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        pair_list = [(nums[i],i) for i in range(n)]
        pair_sorted = sorted(pair_list)
        ans = []
        while l < r:
            cur_sum = pair_sorted[l][0] + pair_sorted[r][0]
            if  cur_sum == target:
                ans.append(pair_sorted[l][1])
                ans.append(pair_sorted[r][1])
                return ans
            elif cur_sum < target:
                l+=1
            else:
                r-=1
