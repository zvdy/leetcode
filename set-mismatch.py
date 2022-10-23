class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                break
        for i in range(1, n+1):
            if i not in nums:
                res.append(i)
                break
        return res