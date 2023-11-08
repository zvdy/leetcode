class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Calculate the absolute difference between the start and finish x-coordinates
        # This represents the width of the grid
        width = abs(sx - fx)
        
        # Calculate the absolute difference between the start and finish y-coordinates
        # This represents the height of the grid
        height = abs(sy - fy)
        
        # If the start and finish points are the same and the time is 1,
        # the cell is not reachable because it takes at least 1 time unit to move to a cell
        if width == 0 and height == 0 and t == 1:
            return False
        
        # The cell is reachable if the time is greater than or equal to the maximum of the width and height
        # This is because it takes at least max(width, height) time units to reach the cell
        return t >= max(width, height)