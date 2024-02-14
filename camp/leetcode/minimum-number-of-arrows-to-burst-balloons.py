class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda x: x[1])
        count = 0
        end = float('-inf')

        for point in points:
            if point[0] > end:
                end = point[1]
                count += 1
        return count
