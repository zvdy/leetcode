class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        return ''.join([c * d[c] for c in sorted(d, key=d.get, reverse=True)])