class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        curr, ans = [], [0] * n

        for i in range(n):
            val = obstacles[i]
            if len(curr) == 0 or curr[-1] <= val:
                curr.append(val)
                ans[i] = len(curr)
            else:
                ind = bisect_right(curr, val, 0, len(curr) - 1)
                curr[ind] = val
                ans[i] = ind + 1
        return ans