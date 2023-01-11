class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_len = 1
        for num in nums:
            if num - 1 not in nums:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in nums:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len