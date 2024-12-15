from typing import *
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 1. get the frequency of each element in arr1
        # 2. sort the elements in arr1 by the order in arr2
        # 3. sort the elements in arr1 by the order in arr1
        # 4. return the sorted arr1
        # 1. get the frequency of each element in arr1
        freq = {}
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # 2. sort the elements in arr1 by the order in arr2
        arr1 = []
        for num in arr2:
            arr1 += [num] * freq[num]
        # 3. sort the elements in arr1 by the order in arr1
        for num in sorted(freq.keys()):
            if num not in arr2:
                arr1 += [num] * freq[num]
        # 4. return the sorted arr1
        return arr1