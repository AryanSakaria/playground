class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # if len(times) == 1:
        #     return 0
        graph = collections.defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
        from queue import PriorityQueue
        p_q = PriorityQueue()
        p_q.put((0, k))
        res = [float("inf") for i in range(n)]
        visit_set = set()
        while len(visit_set) < n and not p_q.empty():
            w, node = p_q.get()
            if node in visit_set:
                continue
            visit_set.add(node)
            res[node-1] = min(res[node-1], w)
            for nei in graph[node]:
                p_q.put((w + nei[1], nei[0]))
            
        res = max(res)
        return res if res!=float("inf") else -1
