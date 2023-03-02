class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        i = 0
        j = 0
        while j < len(chars):
            chars[i] = chars[j]
            count = 0
            while j < len(chars) and chars[j] == chars[i]:
                count += 1
                j += 1
            if count > 1:
                for c in str(count):
                    i += 1
                    chars[i] = c
            i += 1
        return i