class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        return -1