from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return
            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    continue
                dfs(remain - item, stack + [item])
        dfs(target, [])
        return result