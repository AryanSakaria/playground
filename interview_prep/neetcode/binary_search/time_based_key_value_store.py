class TimeMap:

    def __init__(self):
        self.db = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.db:
            self.db[key] = []
        self.db[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.db:
            return ""
        else:
            ans = ""
            l, r = 0, len(self.db[key])-1
            while l <=r:
                mid = l + r
                mid = mid // 2
                if self.db[key][mid][0] <= timestamp:
                    ans = self.db[key][mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)