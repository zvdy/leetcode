class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.index = 0

    
    def visit(self, url: str) -> None:

        for _ in range(len(self.stack) - self.index - 1):
            self.stack.pop()
            
        self.stack.append(url)

        self.index += 1

    def back(self, steps: int) -> str:
        
        if self.stack:
            self.index = max(0, self.index - steps)
            return self.stack[self.index]

    def forward(self, steps: int) -> str:
        
        if self.stack:
            self.index = min(len(self.stack) - 1, self.index + steps)
            return self.stack[self.index]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)