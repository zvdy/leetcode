from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(remain, stack, index):
            if remain == 0:
                result.append(stack)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], stack + [candidates[i]], i + 1)
        dfs(target, [], 0)
        return result