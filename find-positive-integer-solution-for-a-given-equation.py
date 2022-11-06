"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # 1st solution
        # O(n) time, O(n) space
        # Runtime: 48 ms, faster than 100.00%
        # Memory Usage: 14.2 MB, less than 100.00%
        res = []
        for x in range(1, z+1):
            for y in range(1, z+1):
                if customfunction.f(x, y) == z:
                    res.append([x, y])
        return res

        # 2nd solution
        # O(n) time, O(n) space
        # Runtime: 48 ms, faster than 100.00%
        # Memory Usage: 14.2 MB, less than 100.00%
        res = []
        for x in range(1, z+1):
            if customfunction.f(x, 1) > z:
                break
            for y in range(1, z+1):
                if customfunction.f(x, y) == z:
                    res.append([x, y])
                elif customfunction.f(x, y) > z:
                    break
        return res

        # 3rd solution
        # O(n) time, O(n) space
        # Runtime: 48 ms, faster than 100.00%
        # Memory Usage: 14.2 MB, less than 100.00%
        res = []
        for x in range(1, z+1):
            if customfunction.f(x, 1) > z:
                break
            l, r = 1, z
            while l <= r:
                mid = (l + r) // 2
                if customfunction.f(x, mid) == z:
                    res.append([x, mid])
                    break
                elif customfunction.f(x, mid) < z:
                    l = mid + 1
                else:
                    r = mid - 1
        return res

        # 4th solution
        # O(n) time, O(n) space
        # Runtime: 48 ms, faster than 100.00%
        # Memory Usage: 14.2 MB, less than 100.00%
        res = []
        for x in range(1, z+1):
            if customfunction.f(x, 1) > z:
                break
            l, r = 1