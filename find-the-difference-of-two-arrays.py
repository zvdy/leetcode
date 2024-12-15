from typing import *
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output=[]
        output1=set()
        output2=set()
        x=max(len(nums1),len(nums2))
        i=0
        while i<x:
            if (i<len(nums1) and (nums1[i] not in nums2)):
                output1.add(nums1[i])
            if (i<len(nums2) and (nums2[i] not in nums1)):
                output2.add(nums2[i])
            i+=1
        output.append(output1)
        output.append(output2)
        return output
