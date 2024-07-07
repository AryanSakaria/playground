class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r
            mid = mid // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l]    