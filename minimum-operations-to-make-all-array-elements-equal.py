from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [None] * len(queries)

        n = len(nums)
        arr = sorted(nums)
        

        prefix_sum = [None] * n
        prefix_sum[0] = arr[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1]+arr[i]



        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            k = bisect_left(arr, q)
            if k > (n-1):
                k = n-1
            ans[i] = (abs(q-arr[k])) + \
                    (k*q - prefix_sum[k-1] if k > 0 else 0) + \
                    (prefix_sum[-1]-prefix_sum[k]-(n-k-1)*q)


        return ans
