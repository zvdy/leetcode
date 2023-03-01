class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            while left and right:
                if left[0] <= right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            if left:
                res += left
            if right:
                res += right
            return res
        def sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = sort(nums[:mid])
            right = sort(nums[mid:])
            return merge(left, right)
        return sort(nums)