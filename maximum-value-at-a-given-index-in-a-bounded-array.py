class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def helper(mid):
            left = index
            right = n - index - 1
            bound = mid - 1
            l_max = r_max = 0
            if left < bound:
                l_max = t_sum(bound) - t_sum(bound - left)
            else:
                l_max = t_sum(bound) + (left - bound)
            if right < bound:
                r_max = t_sum(bound) - t_sum(bound - right)
            else:
                r_max = t_sum(bound) + (right - bound)
            total = mid + l_max + r_max
            return total <= maxSum
        def t_sum(n):
            return n * (n+1) // 2

        l = 1
        r = maxSum
        while l < r:
            m = (l + r) // 2 + 1 
            if helper(m):
                l = m
            else:
                r = m -1
        return r