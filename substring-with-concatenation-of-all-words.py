from typing import *
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        word_total_len = word_len * word_count
        word_freq = collections.Counter(words)
        result = []

        for i in range(len(s) - word_total_len + 1):
            seen = collections.defaultdict(int)
            for j in range(i, i + word_total_len, word_len):
                word = s[j:j + word_len]
                if word in word_freq:
                    seen[word] += 1
                    if seen[word] > word_freq[word]:
                        break
                else:
                    break
            else:
                result.append(i)

        return result