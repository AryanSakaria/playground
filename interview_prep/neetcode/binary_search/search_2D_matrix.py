class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            mid = l + r
            mid = mid // 2
            cur_element = matrix[mid // n][mid%n]
            if cur_element == target:
                return True
            if cur_element > target:
                r = mid - 1
            else:
                l = mid + 1
        return False