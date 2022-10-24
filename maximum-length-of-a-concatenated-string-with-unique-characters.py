class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(arr, i, s):
            if i == len(arr):
                return len(s)
            if len(set(s + arr[i])) == len(s) + len(arr[i]):
                return max(dfs(arr, i + 1, s + arr[i]), dfs(arr, i + 1, s))
            else:
                return dfs(arr, i + 1, s)
        return dfs(arr, 0, '')