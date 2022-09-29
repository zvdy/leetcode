class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = [1, 1]
        for i in range(2, rowIndex + 1):
            row = [1] + [row[j] + row[j + 1] for j in range(i - 1)] + [1]
        return row