class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf") for _ in range(n)]
        price[src] = 0


        for i in range(k+1):
            tempPrice = price.copy()
            for edge in flights:                
                a,b,w = edge
                if price[a] == float("inf"):
                    continue
                if price[a] + w < tempPrice[b]:
                    tempPrice[b] =  price[a] + w
            price = tempPrice

        return price[dst] if price[dst]!=float("inf") else -1
        