class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort the array by the number of 1 bits in each element, then by the element itself
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))