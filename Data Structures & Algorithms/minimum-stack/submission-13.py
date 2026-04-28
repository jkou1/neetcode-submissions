class MinStack:

    def __init__(self):
        self.minStack = []
        self.curMin = float('inf')
        self.minList = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if val < self.curMin:
            self.curMin = val
        self.minList.append(self.curMin)
        
        

    def pop(self) -> None:
        self.minStack.pop()
        self.minList.pop()
        if self.minList:
            self.curMin = self.minList[-1]
        else:
            self.curMin = float('inf')
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.curMin

        
