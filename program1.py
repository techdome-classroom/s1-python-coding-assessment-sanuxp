class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(row, column):
            if row<0 or row == m or column<0 or column == n or grid[row][column] == 'W':
                return
            grid[row][column] = 'W'