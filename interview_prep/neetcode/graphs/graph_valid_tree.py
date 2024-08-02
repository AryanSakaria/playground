class Solution:
    def dfs(self, node, parent):
        self.visit_set.add(node)
        for child in self.graph[node]:
            if child == parent:
                continue
            if child in self.visit_set:
                self.has_cycle = True
                return
            self.dfs(child, node)
            
            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #create adj list
        self.graph = [[] for _ in range(n)]
        self.visit_set = set()
        self.has_cycle = False
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        self.dfs(0, -1)
        if len(self.visit_set) != n:
            return False
        return not self.has_cycle 
