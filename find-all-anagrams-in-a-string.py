class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        res = []
        if p_count == s_count:
            res.append(0)
        for i in range(1,len(s)-len(p)+1):
            s_count[s[i-1]] -= 1
            if s_count[s[i-1]] == 0:
                del s_count[s[i-1]]
            s_count[s[i+len(p)-1]] += 1
            if p_count == s_count:
                res.append(i)
        return res