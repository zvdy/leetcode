class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        k -= arr[0] - 1
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] - 1 >= k:
                return arr[i] + k
            k -= arr[i + 1] - arr[i] - 1
        return arr[-1] + k