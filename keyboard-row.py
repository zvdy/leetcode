class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(row):
                    res.append(word)
                    break
        return res