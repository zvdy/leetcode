class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return len(s)
        else:
            max_len = 0
            end = len(s)
            while stack:
                start = stack.pop()
                max_len = max(max_len, end - start - 1)
                end = start
            max_len = max(max_len, end)
            return max_len