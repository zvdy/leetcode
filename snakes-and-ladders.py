class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get(x):
            quot, rem = divmod(x - 1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col
        queue = collections.deque([(1, 0)])
        seen = {1}
        while queue:
            num, moves = queue.popleft()
            if num == n * n: return moves
            for x in range(num + 1, min(num + 6, n * n) + 1):
                r, c = get(x)
                if board[r][c] > 0:
                    x = board[r][c]
                if x not in seen:
                    seen.add(x)
                    queue.append((x, moves + 1))
        return -1