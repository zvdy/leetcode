from typing import *
class Solution:
    def largestInteger(self, num: int) -> int:

        mapping_dict = {str(i) : i for i in range(0, 10)}

        odd = []
        even = []

        str_num = str(num)
        for char in str_num:
            if mapping_dict[char] % 2 == 0:
                even.append(mapping_dict[char])
            else:
                odd.append(mapping_dict[char])
        odd.sort(); even.sort()

        integer = 0; odd_count = 0; even_count = 0
        for idx, char in enumerate(str_num[::-1]):
            if mapping_dict[char] % 2 == 0:
                integer += (pow(10, idx) * even[even_count]) 
                even_count += 1
            else:
                integer += (pow(10, idx) * odd[odd_count]) 
                odd_count += 1
        
        return integer


