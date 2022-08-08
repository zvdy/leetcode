class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                for perm in self.permute(nums[:i] + nums[i+1:]):
                    result.append([nums[i]] + perm)
            return result
            