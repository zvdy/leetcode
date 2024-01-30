class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack
        stack = []
        
        # Iterate over each token in the input list
        for token in tokens:
            # If the token is an operator
            if token in '+-*/':
                # Pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation and push the result back onto the stack
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Note: we use int division to discard the fractional part
                    stack.append(int(a / b))
            else:
                # If the token is a number, push it onto the stack
                stack.append(int(token))
        
        # The final result is the only element left in the stack
        return stack.pop()
