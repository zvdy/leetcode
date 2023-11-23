class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Initialize the result list
        res = []
        
        # Iterate over the range of the length of the list l
        for i in range(len(l)):
            # Get the subarray from nums using the indices from l and r and sort it
            sub = sorted(nums[l[i]:r[i]+1])
            
            # Calculate the difference between the first two elements of the subarray
            diff = sub[1] - sub[0]
            
            # Initialize the flag as True
            flag = True
            
            # Iterate over the range of the length of the subarray
            for j in range(1, len(sub)):
                # If the difference between the current and the previous element is not equal to the calculated difference
                # Set the flag as False and break the loop
                if sub[j] - sub[j-1] != diff:
                    flag = False
                    break
            
            # Append the flag to the result list
            res.append(flag)
        
        # Return the result list
        return res