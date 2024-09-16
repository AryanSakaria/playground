class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dist_arr = [1 for _ in range(n)]

        for i in range(m-1):
            for j in range(1, n):
                dist_arr[j] = dist_arr[j] + dist_arr[j-1]
        return dist_arr[-1]
        