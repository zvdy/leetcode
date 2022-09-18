class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(remain, stack):
            if not remain:
                result.append(stack)
                return
            for i in range(len(remain)):
                if i > 0 and remain[i] == remain[i - 1]:
                    continue
                dfs(remain[:i] + remain[i + 1:], stack + [remain[i]])
        dfs(nums, [])
        return result