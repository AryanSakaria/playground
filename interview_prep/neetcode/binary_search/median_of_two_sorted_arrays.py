class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = sorted((nums1,nums2), key = len) #take the smaller array
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            i = (l + r)//2
            j = half - 1 - (i + 1) # simplifies to half - 2
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j+1] if j+1 < len(B) else float("infinity")
            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i+1] if i + 1 < len(A) else float("infinity")
            if B_left <= A_right and A_left <= B_right:
                if total%2:
                    return min(B_right, A_right)
                return (max(A_left, B_left) + min(A_right, B_right))/2
            elif B_left > A_right:
                l = i + 1
            else:
                r = i - 1