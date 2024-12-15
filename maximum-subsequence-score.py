from typing import *
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        idxs = [x for x  in range(n)]
        idxs.sort(key=lambda x: -nums2[x])
        sub = [nums1[idxs[x]] for x in range(k)]
        heapq.heapify(sub)
        cur = sum(sub)*nums2[idxs[k-1]]
        ans = cur
        for i in range(k, n):
            if cur == 0:
                return ans
            j = idxs[i]
            i1 = nums1[j]
            i2 = nums2[j]
            l1 = heapq.heappop(sub)
            heapq.heappush(sub, i1)
            cur = cur / nums2[idxs[i-1]]
            cur = cur - l1 + i1
            cur = cur*i2
            ans = max(ans, cur)
        return int(ans)