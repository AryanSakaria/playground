class Solution:
    def __init__(self):
        self.ans = [[]]
        self.stack = []

    def dfs(self, l):
        if l == len(self.nums):
            return
        
        self.stack.append(self.nums[l])
        self.ans.append(self.stack.copy())
        self.dfs(l+1)
        self.stack.pop()
        l += 1
        while l < len(self.nums) and self.nums[l] ==self.nums[l-1]:
            l+=1
        self.dfs(l)
        return
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        self.nums = sorted(nums)    
        self.dfs(0)
        return self.ans
        