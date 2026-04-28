class MinStack:

    def __init__(self):
        self.stack = []
        self.minlist = []
        self.minimum = float('inf')


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum >= val:
            self.minlist.append(val)
            self.minimum = val

    def pop(self) -> None:
        
        if self.stack[-1] == self.minimum and len(self.minlist) > 1:
            self.minlist.remove(self.minlist[-1])
            self.minimum = self.minlist[-1]
        
        elif self.stack[-1] == self.minimum:
            if len(self.stack) > 1:
                self.minlist.remove(self.minlist[-1])
                self.minimum = self.minlist[-1]
            else: 
                self.minimum = float('inf')
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
