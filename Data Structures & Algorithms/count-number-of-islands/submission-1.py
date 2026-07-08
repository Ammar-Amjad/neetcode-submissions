class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(x, y):
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = deque([(x, y)])

            while queue:
                x, y = queue.popleft()
                
                for dx, dy in dir:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == '1':
                        grid[x + dx][y + dy] = "0"
                        queue.append((x + dx, y + dy)) 

            return 

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    grid[row][col] = "0"
                    bfs(row, col)
                        
        return count