class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sz = len(senate)
        r, d = [], []
        n = sz
        for i in range(sz):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        while len(r) and len(d):
            if r[0] < d[0]:
                r.append(n)
            else:
                d.append(n)
            r.pop(0)
            d.pop(0)
            n += 1
        return "Radiant" if len(r) else "Dire"
