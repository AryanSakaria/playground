class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans_set = []
        a, b, c = 0,0,0

        for trip in triplets:
            if trip[0] > target[0]:
                continue
            if trip[1] > target[1]:
                continue
            if trip[2] > target[2]:
                continue
            ans_set.append(trip)
            a = max(a, trip[0])
            b = max(b, trip[1])
            c = max(c, trip[2])
        
        if a < target[0] or b < target[1] or c < target[2]:
            return False

        return True
