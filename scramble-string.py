class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if len(s1)==1:
            return s1==s2
        l=len(s1)
        for i in range(1,l):
            #case that we don't switch
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            #case that we do switch
            if self.isScramble(s1[:i], s2[l-i:]) and self.isScramble(s1[i:], s2[:l-i]):
                return True
        return False