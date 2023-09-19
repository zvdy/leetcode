class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare (Cycle Detection)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder: break
        return slow