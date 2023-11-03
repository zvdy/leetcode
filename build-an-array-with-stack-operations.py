class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # Initialize the stack and the answer list
        stack = []
        ans = []
        # Iterate over the range from 1 to n+1
        for i in range(1, n + 1):
            # If the current number is in the target list, append it to the stack and add "Push" to the answer list
            if i in target:
                stack.append(i)
                ans.append("Push")
            # If the current number is not in the target list, add "Push" and "Pop" to the answer list
            else:
                ans.append("Push")
                ans.append("Pop")
            # If the stack is equal to the target list, return the answer list
            if stack == target:
                return ans
        # If the loop completes without returning, return the answer list
        return ans