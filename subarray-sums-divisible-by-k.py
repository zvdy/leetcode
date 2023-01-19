class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        count = 0
        mod = 0
        d = {0: 1}
        for num in nums:
            mod = (mod + num) % k
            if mod in d:
                count += d[mod]
                d[mod] += 1
            else:
                d[mod] = 1
        return count