class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from queue import PriorityQueue
        from collections import deque

        count_dict = {}
        for task in tasks:
            count_dict[task] = 1 + count_dict.get(task, 0)
        
        max_heap = PriorityQueue()
        for key_ in count_dict:
            max_heap.put(-count_dict[key_])
        
        q_rem = deque()

        time = 0
        while not max_heap.empty() or len(q_rem):
            # print(time)
            time += 1
            if not max_heap.empty():
                top_task = -max_heap.get()
                top_task -= 1
                if top_task:
                    q_rem.append((time + n, top_task))
            if len(q_rem) and q_rem[0][0] == time:
                    _, task = q_rem.popleft()
                    max_heap.put(-task)
        return time
        