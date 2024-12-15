from typing import *
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_group = {}
        idx = 0
        char_map = {chr(97 + i): -1 for i in range(26)}

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue

            if char_map[s1[i]] == -1 and char_map[s2[i]] == -1:
                char_map[s1[i]] = char_map[s2[i]] = idx
                char_group[idx] = [s2[i], s1[i]]
                idx += 1
            elif char_map[s1[i]] == -1:
                char_map[s1[i]] = char_map[s2[i]]
                char_group[char_map[s2[i]]].append(s1[i])
            elif char_map[s2[i]] == -1:
                char_map[s2[i]] = char_map[s1[i]]
                char_group[char_map[s1[i]]].append(s2[i])
            elif char_map[s1[i]] != char_map[s2[i]]:
                for c in char_group[char_map[s2[i]]]:
                    char_map[c] = char_map[s1[i]]
                    char_group[char_map[s1[i]]].append(c)

        for k in char_group.keys():
            char_group[k].sort()

        ans = ""
        for c in baseStr:
            if char_map[c] == -1:
                ans += c
            else:
                ans += char_group[char_map[c]][0]

        return ans