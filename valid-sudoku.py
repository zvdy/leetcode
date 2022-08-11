class Solution(object):
    def isValidSudoku(self, board):
        heap_row = collections.defaultdict(list)
        heap_col = collections.defaultdict(list)
        grid = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    m = i//3
                    n = j//3
                    g = m*3 + n
                    grid[g].append(board[i][j])
                    heap_row[i].append(board[i][j])
                    heap_col[j].append(board[i][j])
        for i in heap_row:
            if len(heap_row[i]) != len(set(heap_row[i])):
                return False
        for i in heap_col:
            if len(heap_col[i]) != len(set(heap_col[i])):
                return False
        for i in grid:
            if len(grid[i]) != len(set(grid[i])):
                return False
        return True