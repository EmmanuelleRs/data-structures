class Stack():
    def __init__(self) -> None:
        self.stack = []
        self.maxMinStack = []

    def peak(self):
        return self.stack[len(self.stack) - 1]
    
    def pop(self):
        self.maxMinStack.pop()
        return self.stack.pop()
    
    def push(self, num):
        #push and element and track te max and min elelment on the stack
        newMaxMin = {'min': num, 'max': num}
        if len(self.stack):
            currentMaxMin = self.maxMinStack[len(self.maxMinStack) - 1]
            newMaxMin['min'] = min(num, currentMaxMin["min"])
            newMaxMin['max'] = max(num, currentMaxMin["max"])
        self.maxMinStack.append(newMaxMin)
        self.stack.append(num)

    def getMin(self):
        return self.maxMinStack[len(self.maxMinStack) - 1]['min']
    
    def getMax(self):
        return self.maxMinStack[len(self.maxMinStack) - 1]['max']

