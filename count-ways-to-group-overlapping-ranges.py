class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        end_max, res = -1, 1
        for start_i, end_i in sorted(ranges):
            res = res * (2 if end_max < start_i else 1) % 1000000007
            end_max = max(end_max, end_i)
        return res