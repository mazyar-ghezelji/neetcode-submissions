class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # invalid cases
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if grid[r][c] == 1:  # rock or visited
                return 0
            
            # reached destination
            if r == rows - 1 and c == cols - 1:
                return 1
            
            # mark as visited
            grid[r][c] = 1
            
            # explore all directions
            paths = (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
            
            # backtrack
            grid[r][c] = 0
            
            return paths
        
        return dfs(0, 0)