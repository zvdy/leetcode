from typing import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        for i in range(len(s)):
            temp=s[i]
            for j in range(i+1,len(s)):
                if(s[j] in temp):
                    break
                temp+=s[j]
            if(len(temp)>len(res)):
                res=temp
        return len(res)