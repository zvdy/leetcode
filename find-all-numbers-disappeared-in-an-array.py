
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set() # init  a set to store unique values to compare with the range of the list
        result = [] 

        # populate the set with unique values
        for i in nums:
            print(i)
            uniq.add(i)

        # compare the set with the range of the list and append the missing values to the result list
        for j in range(1, len(nums) + 1): 
            print(j)
            if j not in uniq:
                result.append(j)

        return result