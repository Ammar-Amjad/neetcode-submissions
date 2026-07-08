class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            
            grid[x][y] = 0
            # go down
            if 0 <= x + 1 < len(grid) and grid[x+1][y] == "1":
                dfs(x + 1, y)
            # go right
            if 0 <= y + 1 < len(grid[0]) and grid[x][y+1] == "1":
                dfs(x, y + 1)
            # go left
            if 0 <= y - 1 < len(grid[0]) and grid[x][y-1] == "1":
                dfs(x, y - 1)
            # go top
            if 0 <= x - 1 < len(grid) and grid[x-1][y] == "1":
                dfs(x - 1, y)

            return 

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        
        return count