class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(queries)):
            sum = 0
            count = 0
            for j in range(len(nums)):
                if sum+nums[j]<=queries[i]:
                    sum += nums[j]
                    count += 1
                else:
                    break
            ans.append(count)        
       
        return ans

