class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = []
        n = len(heights)
        ans = 0
        for i in range(n):
            x = heights[i]
            cur_index = i
            while stack and stack[-1][0] > x:
                ans = max(ans, (i - stack[-1][1])*stack[-1][0])
                cur_index = stack[-1][1]
                stack.pop()
            stack.append((x, cur_index))
        return ans