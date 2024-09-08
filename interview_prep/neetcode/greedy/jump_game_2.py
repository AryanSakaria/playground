class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r < len(nums)-1:
            max_so_far = r
            for i in range(l,r+1):
                max_so_far = max(max_so_far, i + nums[i])
            l = r + 1
            r = max_so_far
            count += 1
        return count


        