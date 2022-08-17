class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in count[:k]]