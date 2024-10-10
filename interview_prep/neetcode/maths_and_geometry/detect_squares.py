class DetectSquares:

    def __init__(self):
        self.map_count = {}

    def add(self, point: List[int]) -> None:
        self.map_count[tuple(point)] = 1 + self.map_count.get(tuple(point), 0)

    def count(self, point: List[int]) -> int:
        ans = 0
        for point_ in self.map_count:
            dist_x = abs(point_[0] - point[0])
            dist_y = abs(point_[1] - point[1])
            if dist_x != dist_y:
                continue
            if dist_x == 0:
                continue
            if (point[0], point_[1]) in self.map_count and (point_[0], point[1]) in self.map_count:
                ans += self.map_count[point_] * self.map_count[(point[0], point_[1])] * self.map_count[(point_[0], point[1])]
        return ans




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)