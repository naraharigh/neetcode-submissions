class MinStack:

    def __init__(self):
        self.stack_mini = []
        
    def push(self, val: int) -> None:
        self.stack_mini.append(val)
        
    def pop(self) -> None:
        self.stack_mini.pop()
        
    def top(self) -> int:
        l = len(self.stack_mini)
        return self.stack_mini[l-1]
        
    def getMin(self) -> int:
        return min(self.stack_mini)
        
