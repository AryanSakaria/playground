class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare, tortoise = 0, 0
        hare = nums[hare]
        tortoise = nums[nums[tortoise]]

        while hare!=tortoise:
            hare = nums[hare]
            tortoise = nums[nums[tortoise]]

        tortoise = 0
        while hare!=tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare
        