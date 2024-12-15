from typing import *
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.keys():
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        def dfs(letter, cur, depth):
            if not cur: return False
            if letter == '.':
                if depth == len(word):
                    for nxt_c in cur.values():
                        if nxt_c:
                            if '*' in nxt_c.keys():
                                return True
                    return False
                for _, nxt_c in cur.items():
                    # each iteration should be check
                    # so can not return directly
                    if dfs(word[depth], nxt_c, depth+1):
                        return True
                return False
            else:
                if letter not in cur.keys():
                    return False
                else:
                    if depth == len(word):
                        return True if '*' in cur[letter].keys() else False
                    return dfs(word[depth], cur[letter], depth+1)
        return dfs(word[0], self.root, 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)