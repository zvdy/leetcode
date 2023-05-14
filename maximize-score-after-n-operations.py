class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def function(nums,k):
            if not nums:
                return 0

            res=0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    remaining=nums[:i]+nums[i+1:j]+nums[j+1:]
                    res=max(res,k*gcd(nums[i],nums[j])+function(tuple(remaining),k+1))

            return res

        return function(tuple(nums),1)