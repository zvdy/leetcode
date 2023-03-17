class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curLevel = self.trie
        for ch in word:
            if ch not in curLevel:
                curLevel[ch] = {}
            curLevel = curLevel[ch]
        curLevel["#"] = None

    def search(self, word: str) -> bool:
        curLevel = self.trie
        for ch in word:
            if ch in curLevel:
                curLevel = curLevel[ch]
            else:
                return False
        return "#" in curLevel

    def startsWith(self, prefix: str) -> bool:
        curLevel = self.trie
        for ch in prefix:
            if ch in curLevel:
                curLevel = curLevel[ch]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)