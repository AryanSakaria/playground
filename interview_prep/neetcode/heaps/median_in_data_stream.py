class MedianFinder:

    def __init__(self):
        from queue import PriorityQueue
        self.first_half = PriorityQueue()
        self.second_half = PriorityQueue()

        

    def addNum(self, num: int) -> None:
        if not self.first_half.qsize():
            self.first_half.put(-num)
            return
        if not self.second_half.qsize():
            top_f = -self.first_half.get()
            a, b = min(top_f, num), max(top_f, num)
            self.first_half.put(-a)
            self.second_half.put(b)
            return 

        a, b = -self.first_half.get(), self.second_half.get()
        s_nums = sorted([a, num, b])
        if self.first_half.qsize() == self.second_half.qsize():
            self.first_half.put(-s_nums[0])
            self.first_half.put(-s_nums[1])
            self.second_half.put(s_nums[2])
            return
        
        self.first_half.put(-s_nums[0])
        self.second_half.put(s_nums[1])
        self.second_half.put(s_nums[2])
        return
    



        

    def findMedian(self) -> float:
        if not self.second_half.qsize():
            return -self.first_half.queue[0]
        if self.first_half.qsize() == self.second_half.qsize():
            return (-self.first_half.queue[0] + self.second_half.queue[0])/2
        return -self.first_half.queue[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()