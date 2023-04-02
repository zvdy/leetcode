class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)
        for i in spells:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if i * potions[mid] < success:
                    left = mid + 1 
                else:
                    right = mid
            res.append(n - left)
        return res