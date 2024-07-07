class Solution:
    def get_time(self, piles, k):
        time = 0
        for i in piles:
            time += ceil(i/k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = l + r
            mid = mid // 2
            cur_time = self.get_time(piles, mid)
            if cur_time <= h:
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
        return ans