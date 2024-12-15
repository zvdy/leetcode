from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        result = set()
        if nums.count(candidate1) > len(nums) // 3:
            result.add(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            result.add(candidate2)
        return list(result)