class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        pre_sum = 1
        for i in range(n):
            ans.append(pre_sum*nums[i])
            pre_sum *= nums[i]
        suf_sum = 1
        post_sum = nums[-1]
        ans[-1] = ans[n-2]
        for i in range(1,n-1):
            cur_index = n - i - 1
            ans[cur_index] = post_sum * ans[cur_index-1]
            post_sum *= nums[cur_index]
        ans[0] = post_sum
        return ans 
