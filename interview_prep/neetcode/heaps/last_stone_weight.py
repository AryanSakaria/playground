class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from queue import PriorityQueue
        cur_queue = PriorityQueue()
        for stone in stones:
            cur_queue.put(-stone)

        while cur_queue.qsize() >= 2:
            top_stone = -cur_queue.get()
            second_stone = -cur_queue.get()
            if top_stone == second_stone:
                continue
            larger_stone, smaller_stone = max(top_stone, second_stone), min(top_stone, second_stone)
            cur_queue.put(smaller_stone - larger_stone)
        
        if cur_queue.qsize() > 0:
            return -cur_queue.queue[0]
        return 0

