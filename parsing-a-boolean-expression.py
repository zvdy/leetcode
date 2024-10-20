class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

        't' that evaluates to true.
        'f' that evaluates to false.
        '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
        '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
        '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
        """
        def evaluate(expression):
            stack = []
            for char in expression:
                if char == ')':
                    seen = []
                    while stack[-1] != '(':
                        seen.append(stack.pop())
                    stack.pop()  # Remove '('
                    operator = stack.pop()
                    if operator == '!':
                        stack.append('t' if seen[0] == 'f' else 'f')
                    elif operator == '&':
                        stack.append('t' if all(x == 't' for x in seen) else 'f')
                    elif operator == '|':
                        stack.append('t' if any(x == 't' for x in seen) else 'f')
                elif char != ',':
                    stack.append(char)
            return stack[0] == 't'
        
        return evaluate(expression)