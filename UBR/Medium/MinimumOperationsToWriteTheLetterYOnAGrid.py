"""
You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

We say that a cell belongs to the Letter Y if it belongs to one of the following:

The diagonal starting at the top-left cell and ending at the center cell of the grid.
The diagonal starting at the top-right cell and ending at the center cell of the grid.
The vertical line starting at the center cell and ending at the bottom border of the grid.
The Letter Y is written on the grid if and only if:

All values at cells belonging to the Y are equal.
All values at cells not belonging to the Y are equal.
The values at cells belonging to the Y are different from the values at cells not belonging to the Y.
Return the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.

Example 1:
Input: grid = [[1,2,2],[1,1,0],[0,1,0]]
Output: 3
Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.
    1 2 2     1 0 1
    1 1 0     0 1 0
    0 1 0     0 1 0

Example 2:
Input: grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
Output: 12
Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 0 while those that do not belong to Y are equal to 2. 
It can be shown that 12 is the minimum number of operations needed to write Y on the grid.
 

Constraints:
3 <= n <= 49 
n == grid.length == grid[i].length
0 <= grid[i][j] <= 2
n is odd.
"""
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        Y = []
        NoY = []
        n = len(grid)
        for i in range(n//2):
            for j in range(n):
                if i == j or j == n-i-1:
                    Y.append(grid[i][j])
                else:
                    NoY.append(grid[i][j])
        for i in range(n//2, n):
            for j in range(n):
                if j == n//2:
                    Y.append(grid[i][j])
                else:
                    NoY.append(grid[i][j])
        
        counter_Y = Counter(Y)
        counter_NoY = Counter(NoY)
        # print(Y, counter_Y, set(counter_Y))
        # print(NoY, set(counter_NoY))
        if len(set(counter_Y)) == 1 and set(counter_Y) == set(counter_NoY):
            return len(Y)
        sorted_Y_values = sorted(counter_Y.values(), reverse=True)
        sorted_NoY_values = sorted(counter_NoY.values(), reverse=True)

        cal_Y = sorted_Y_values[0]
        cal_NoY = sorted_NoY_values[0]

        max_Y_key = max(counter_Y, key=counter_Y.get)
        max_counter_NoY_key = max(counter_NoY, key=counter_NoY.get)
        # print(cal_Y, cal_NoY)
        res = len(Y) - cal_Y + len(NoY) - cal_NoY
        
        if max_Y_key == max_counter_NoY_key:
            temp_A = sys.maxsize
            temp_B = sys.maxsize
            if len(sorted_Y_values) > 1 :
                temp_A = len(Y) - sorted_Y_values[1] + len(NoY) - cal_NoY
            if len(sorted_NoY_values) > 1 :
                temp_B = len(Y) - cal_Y + len(NoY) - sorted_NoY_values[1]
            res = min(temp_A, temp_B)
        return res

        
