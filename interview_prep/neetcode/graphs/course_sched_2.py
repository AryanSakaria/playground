class Solution:
    def dfs(self, i):
        if self.visit_set[i] == 1:
            self.is_cycle = True
            return True
        if self.visit_set[i] == 2:
            return False
        self.visit_set[i] = 1
        #DFS
        for children in self.graph[i]:
            if self.dfs(children):
                return True
        self.visit_set[i] = 2
        self.ordering.append(i)
        #topological sorting is always reverse of finish time 
        return False
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.is_cycle = False
        self.visit_set = [0 for _ in range(numCourses)]
        self.pre_reqs = prerequisites
        self.graph = [[] for _ in range(numCourses)]
        self.ordering = []
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        for a,b in prerequisites:
            self.graph[b].append(a)

        for i in range(numCourses):
            if self.dfs(i):
                return []
                
        return reversed(self.ordering)
