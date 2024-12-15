from typing import *
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        bank = set(bank)
        queue = deque([(start, 0)])
        while queue:
            gene, level = queue.popleft()
            if gene == end:
                return level
            for i in range(len(gene)):
                for c in "ACGT":
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene in bank:
                        bank.remove(new_gene)
                        queue.append((new_gene, level+1))
        return -1