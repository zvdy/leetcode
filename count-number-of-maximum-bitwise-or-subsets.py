class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def get_max_or(nums):
            max_or = 0
            for num in nums:
                max_or |= num
            return max_or
        
        def count_subsets(nums, max_or):
            count = 0
            n = len(nums)
            for i in range(1, 2**n):
                current_or = 0
                for j in range(n):
                    if i & (1 << j):
                        current_or |= nums[j]
                if current_or == max_or:
                    count += 1
            return count
        
        max_or = get_max_or(nums)
        return count_subsets(nums, max_or)

# time complexity: O(2^n)
# space complexity: O(1)