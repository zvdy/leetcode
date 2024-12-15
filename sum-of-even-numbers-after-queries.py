from typing import *
class Solution:
  def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    ans = []
    summ = sum(a for a in nums if a % 2 == 0)

    for q in queries:
      if nums[q[1]] % 2 == 0:
        summ -= nums[q[1]]
      nums[q[1]] += q[0]
      if nums[q[1]] % 2 == 0:
        summ += nums[q[1]]
      ans.append(summ)

    return ans
