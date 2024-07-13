"""
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

Example 1:
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
(1, 1) (1, 3) (3, 1) (3, 3) 4
(1, 3) (1, 1) (3, 3) (3, 1) 4

Example 2:
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
(1, 1) (1, 3) (3, 1) (3, 3) 4
(1, 1) (1, 3) (4, 1) (4, 3) 6
(1, 3) (1, 1) (3, 3) (3, 1) 4
(1, 3) (1, 1) (4, 3) (4, 1) 6
(3, 1) (3, 3) (4, 1) (4, 3) 2
(3, 3) (3, 1) (4, 3) (4, 1) 2

Constraints:
1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 10**4
All the given points are unique.

"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        min_area = float('inf')
        """
        (x1, y2),(x2, y2)
        (x1, y1),(x2, y1)
        """
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        # print((x1, y1), (x1, y2), (x2, y1), (x2, y2), area)
                        min_area = min(min_area, area)
                
        return min_area if min_area != float('inf') else 0
