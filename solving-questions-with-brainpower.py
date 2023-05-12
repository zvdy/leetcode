class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = defaultdict(int)
        for i in range(n-1, -1, -1):
            points, bp = questions[i]
            dp[i] = max(points + dp[i+bp+1], dp[i+1])
        return dp[0]