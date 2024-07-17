class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from queue import PriorityQueue
        q = PriorityQueue()
        count = 0
        for point in points:
            q.put((point[0]**2 + point[1]**2, count, point))
            count += 1
        
        ans = []
        for i in range(k):
            ans.append(q.get()[2])
        return ans
        