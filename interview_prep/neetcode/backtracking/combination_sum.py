class Solution:
    def __init__(self):
        self.stack = []
        self.ans = []
    def dfs(self,l, target):
        if l == len(self.nums):
            return
        if target == 0:
            self.ans.append(self.stack.copy())
            return
        if target < 0:
            return
        #take the sum
        self.stack.append(self.nums[l])
        self.dfs(l,target - self.nums[l])
        #dont take the sum
        self.stack.pop()
        self.dfs(l+1, target)
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        self.dfs(0, target)
        return self.ans
        