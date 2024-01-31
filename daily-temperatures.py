class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize an empty stack
        stack = []
        
        # Initialize the result list with zeros
        res = [0] * len(temperatures)
        
        # Iterate over the temperatures list with index and value
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the last temperature in the stack
            while stack and t > temperatures[stack[-1]]:
                # Pop the index of the last temperature from the stack
                cur = stack.pop()
                
                # Update the result list at the index of the popped temperature with the difference between the current index and the popped index
                res[cur] = i - cur
            
            # Push the current index to the stack
            stack.append(i)
        
        # Return the result list
        return res
