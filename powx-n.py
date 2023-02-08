class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
        n = abs(n)
        ans = 1
        while n > 0:
            if n & 1:
                ans = x * ans
            x *= x
            n >>= 1
        return ans
