class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(h) < k:
                    heapq.heappush(h, (-nums1[i]-nums2[j], nums1[i], nums2[j]))
                else:
                    if -h[0][0] > nums1[i] + nums2[j]:
                        heapq.heappop(h)
                        heapq.heappush(h, (-nums1[i]-nums2[j], nums1[i], nums2[j]))
                    else:
                        break
        return [[x[1], x[2]] for x in h]