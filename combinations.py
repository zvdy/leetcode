from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def f(i,res):
            if(len(res)==k):
                ans.append(res[:])
            for i in range(i,n+1):
                res.append(i)
                f(i+1,res)
                res.pop()
            return ans
        ans=[]
        f(1,[])
        return ans  