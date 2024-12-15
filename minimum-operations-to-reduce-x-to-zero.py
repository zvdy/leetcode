from typing import *
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Find the longest subarray with sum(nums) - x
        # If such subarray exists, return len(nums) - len(subarray)
        # Else return -1
        target = sum(nums) - x
        if target == 0: return len(nums)
        if target < 0: return -1
        left = 0
        curr_sum = 0
        max_len = -1
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len != -1 else -1