class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        x = y = dx = 0
        dy = 1
        ans = 0
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        ans = max(ans, x*x + y*y)
        return ans

        