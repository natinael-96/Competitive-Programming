class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minS:
            if val <= self.minS[-1]:
                self.minS.append(val)
        else:
            self.minS.append(val)

    def pop(self) -> None:
        
        if self.stack.pop() == self.minS[-1]:
            self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minS[-1] 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()