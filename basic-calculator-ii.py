class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        num = 0
        op = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == len(s) - 1 or s[i] in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                op = s[i]
        return sum(stack)