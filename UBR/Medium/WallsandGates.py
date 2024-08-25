"""
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 2**31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
 
Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2**31 - 1.
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1
        len_row = len(rooms)
        len_col = len(rooms[0])

        q = deque() # queue for gate
        for r in range(len_row):
            for c in range(len_col):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    
        while q:
            i, j = q.popleft()
            distance = rooms[i][j]+1
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x, y = i+dx, j+dy
                if (0 <= x < len_row and 0 <= y < len_col) and rooms[x][y] == INF: 
                    rooms[x][y] = distance
                    q.append((x, y))
                    # print(x, y, q, distance)
        
                    
