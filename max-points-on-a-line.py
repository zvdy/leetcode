class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            same_points = 1
            slope_dict = {}
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_points += 1
                elif points[i][0] == points[j][0]:
                    slope_dict['inf'] = slope_dict.get('inf', 0) + 1
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    slope_dict[slope] = slope_dict.get(slope, 0) + 1
            max_points = max(max_points, same_points + max(slope_dict.values(), default=0))
        return max_points