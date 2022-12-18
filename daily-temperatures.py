class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res