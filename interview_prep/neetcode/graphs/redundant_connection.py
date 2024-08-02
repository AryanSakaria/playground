class Solution:
    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            parent_x = self.find(self.parent[x])
            self.parent[x] = parent_x
            return parent_x
    
    def union(self,x,y):
        a = self.find(x)
        b = self.find(y)
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        self.rank[a]+=self.rank[b]
        

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        for a,b in edges:
            a, b = a -1, b - 1
            if self.find(a) == self.find(b):
                return [a+1,b+1]
            self.union(a,b)
        

        