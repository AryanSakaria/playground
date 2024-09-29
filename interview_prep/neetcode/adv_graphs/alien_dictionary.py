class Solution:
    def dfs(self, node):
        #determine if cycle 
        #-1 = not visited
        #0 = currently visiting
        #1 = visited

        if self.visit[node] == 0:
            return True
        if self.visit[node] == 1:
            return False
        
        self.visit[node] = 0

        for nei in self.graph[node]:
            if self.dfs(nei):
                return True
        self.res.append(node)
        self.visit[node] = 1
        return False

    def foreignDictionary(self, words: List[str]) -> str:
        graph = {s:set() for w in words for s in w}
        for i in range(len(words)-1):
            a, b = words[i], words[i+1]
            minLen = min(len(a), len(b))
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""
            for k in range(minLen):
                if a[k]!=b[k]:
                    graph[a[k]].add(b[k])
                    break
        self.graph = graph
        self.res = []
        self.visit = {key:-1 for key in graph}
        for char in self.visit:
            if self.dfs(char):
                return ""
        self.res.reverse()
        return "".join(self.res)


