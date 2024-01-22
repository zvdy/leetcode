class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        # Sort the list in ascending order
        nums.sort()
        # Initialize an empty list to store the result
        res = []
        # Iterate over each number in the sorted list (except the last one)
        for i in range(n-1):
            # If the current number is equal to the next number, it's the duplicate number
            # Add it to the result list and stop the loop
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                break
        # Iterate over each number from 1 to n (inclusive)
        for i in range(1, n+1):
            # If a number is not in the input list, it's the missing number
            # Add it to the result list and stop the loop
            if i not in nums:
                res.append(i)
                break
        # Return the result list, which contains the duplicate number and the missing number
        return res
