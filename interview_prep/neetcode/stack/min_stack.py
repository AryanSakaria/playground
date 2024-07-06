class MinStack:

    def __init__(self):
        self.array = []
        

    def push(self, val: int) -> None:
        if not self.array:
            self.array.append((val,val))
        else:
            self.array.append((val, min(val,self.array[-1][1])))
        

    def pop(self) -> None:
        self.array.pop()
        

    def top(self) -> int:
        return self.array[-1][0]
        

    def getMin(self) -> int:
        return self.array[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()