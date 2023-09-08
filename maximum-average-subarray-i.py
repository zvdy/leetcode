class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == k:
            return sum(nums) / k
        max_sum = sum(nums[0:k])
        curr_sum = max_sum
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k