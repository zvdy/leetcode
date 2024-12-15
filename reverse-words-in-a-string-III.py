from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s1 = ""
        for i in s:
            count = len(i)
            s1 += " "
            while count > 0:
                s1 += i[count - 1]
                count -= 1
        return s1.strip()