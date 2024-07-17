class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()

        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()

        return q.get()
        