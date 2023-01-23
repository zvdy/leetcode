class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trust_count = [0] * (n + 1)
        for i, j in trust:
            trust_count[i] -= 1
            trust_count[j] += 1
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        return -1