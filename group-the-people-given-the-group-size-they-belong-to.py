class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = [i]
            else:
                d[groupSizes[i]].append(i)
        res = []
        for key in d:
            if len(d[key]) == key:
                res.append(d[key])
            else:
                for i in range(0, len(d[key]), key):
                    res.append(d[key][i:i+key])
        return res