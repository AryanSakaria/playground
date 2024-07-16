class Solution:
    def dfs(self, i, target):
        
        if target == 0:
            self.ans.append(self.stack.copy())
            return
        if i >= len(self.nums) or target < 0:
            return
        
        
        #take
        self.stack.append(self.nums[i])
        self.dfs(i+1, target - self.nums[i])
        self.stack.pop()
        #don't take
        i+=1
        while i < len(self.nums) and self.nums[i] == self.nums[i-1]:
            i+=1
        self.dfs(i, target)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.stack = []
        self.ans = []
        self.nums = sorted(candidates)
        self.dfs(0, target)
        return self.ans
