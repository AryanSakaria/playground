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
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.is_cycle = False
        self.visit_set = [0 for _ in range(numCourses)]
        self.pre_reqs = prerequisites
        self.graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            self.graph[b].append(a)

        for i in range(numCourses):
            if self.dfs(i):
                return False
                
        return True