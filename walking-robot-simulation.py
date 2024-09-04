class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert list of obstacles to a set of tuples for faster lookup
        obstacles = set(map(tuple, obstacles))
        
        # Initialize starting position and direction
        x = y = dx = 0
        dy = 1
        ans = 0
        
        # Iterate through each command
        for command in commands:
            if command == -2:  # Turn left
                dx, dy = -dy, dx
            elif command == -1:  # Turn right
                dx, dy = dy, -dx
            else:  # Move forward
                for _ in range(command):
                    # Check if the next position is not an obstacle
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        # Update the maximum Euclidean distance squared
                        ans = max(ans, x*x + y*y)
        
        # Return the maximum Euclidean distance squared
        return ans