class Solution:
    def dfs(self, airport):
        while self.graph[airport]:
            candidate = self.graph[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.route = []
        for a, b in tickets:
            self.graph[a].append(b)
        for city in self.graph:
            self.graph[city] = sorted(self.graph[city], reverse = True)
        self.dfs("JFK")
        return self.route[::-1]
