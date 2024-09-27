class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(row, column):
            if row<0 or row == m or column<0 or column == n or grid[row][column] == 'W':
                return
            grid[row][column] = 'W'
            dfs(row+1, column)
            dfs(row-1, column)
            dfs(row, column+1)
            dfs(row, column-1)
        count = 0
        for row in range(m):
            for column in range(n):
                if grid[row][column]=='L':
                    dfs(row, column)
                count+=1
        return count
if __name__ == "__main__":
    s = Solution()