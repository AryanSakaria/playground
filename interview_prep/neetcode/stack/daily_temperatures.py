class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        
        for i, temp_ in enumerate(temperatures):
            while stack and temp_ > stack[-1][0]:
                cur_idx = stack[-1][1]
                ans[cur_idx] = i - cur_idx
                stack.pop()

            stack.append((temp_, i)) 
        return ans