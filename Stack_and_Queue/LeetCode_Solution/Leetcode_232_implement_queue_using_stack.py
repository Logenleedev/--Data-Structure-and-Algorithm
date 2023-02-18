class MyQueue:
    
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        if self.empty() == True:
            return None
        
        if len(self.stack_out) != 0:
            return self.stack_out.pop()
        
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self) -> bool:
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)