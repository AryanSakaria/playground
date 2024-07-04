class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [],[]
        n = len(height)
        for i in range(n):
            if i == 0:
                max_l.append(height[i])
                max_r.append(height[n-1-i])
            else:
                max_l.append(max(max_l[i-1], height[i]))
                max_r.append(max(max_r[i-1], height[n-1-i]))
        max_r.reverse() 
        ans = 0
        for i in range(n):
            ans += max(min(max_l[i], max_r[i]) - height[i] , 0)
        return ans