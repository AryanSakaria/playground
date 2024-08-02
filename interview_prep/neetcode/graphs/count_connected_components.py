class Solution:
    def dfs(self, node):
        if node in self.visit_set:
            return
        self.visit_set.add(node)
        for child in self.graph[node]:
            self.dfs(child)
        return
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = [[] for _ in range(n)]
        self.visit_set = set()
        connectedComponents = 0

        for a,b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        for i in range(n):
            if i in self.visit_set:
                continue
            connectedComponents += 1
            self.dfs(i)
        return connectedComponents
        