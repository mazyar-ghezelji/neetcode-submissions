class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins)==0:
            self.mins.append(val)
        else:
            if val<=self.mins[-1]:
                self.mins.append(val)
        return 
    def pop(self) -> None:
        if self.stack[-1]==self.mins[-1]:
            self.mins.pop(-1)
        self.stack.pop(-1)
        return
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
