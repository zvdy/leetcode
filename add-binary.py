from typing import *
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = ''
        for i in range(len(b)):
            sum = int(a[i]) + int(b[i]) + carry
            carry = sum // 2
            result += str(sum % 2)
        for i in range(len(b), len(a)):
            sum = int(a[i]) + carry
            carry = sum // 2
            result += str(sum % 2)
        if carry:
            result += '1'
        return result[::-1]