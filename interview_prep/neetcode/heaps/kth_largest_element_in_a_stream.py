class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from queue import PriorityQueue
        self.q = PriorityQueue()
        for num in nums:
            self.q.put(num)
        while self.q.qsize() > k:
            self.q.get()
        self.k = k

        

    def add(self, val: int) -> int:
        if self.q.qsize() < self.k:
            self.q.put(val)
            return self.q.queue[0]
         
        if val > self.q.queue[0]:
            self.q.put(val)
            self.q.get()
        return self.q.queue[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)