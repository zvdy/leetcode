from typing import *
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        i, flag = 0, -1
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(rows)