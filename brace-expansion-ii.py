from typing import *
class Parser:
    def __init__(self, input):
        self.input = input
        self.i = 0

    def parse_expr(self):
        if self.input[self.i] == '{':
            ret = set()
            self.i += 1

            while self.i < len(self.input) and self.input[self.i] != '}':
                for i in self.parse_expr():
                    ret.add(i)
                if self.input[self.i] == '}':
                    break
                self.i += 1

            if self.i+1 < len(self.input):
                nextchar = self.input[self.i+1]
                if nextchar == '{' or nextchar.isalpha():
                    self.i += 1
                    adj = self.parse_expr()
                    return [i+j for i in ret for j in adj]

            self.i += 1
            return list(ret)

        else:
            bef = self.i
            while self.i < len(self.input) and self.input[self.i].isalpha():
                self.i += 1

            word = self.input[bef:self.i]
            if self.i < len(self.input) and self.input[self.i] == '{':
                return [word+i for i in self.parse_expr()]
            return [word]

            
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        ans = Parser(expression).parse_expr()
        return sorted(ans)

