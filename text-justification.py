from typing import *
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_lines = []
        line = []
        line_length = 0
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                spaces = maxWidth - line_length
                for i in range(spaces):
                    line[i % (len(line) - 1 or 1)] += ' '
                justified_lines.append(''.join(line))
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        justified_lines.append(last_line)
        return justified_lines
