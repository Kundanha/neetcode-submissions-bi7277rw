class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            perimeter = dfs(r, c+1) + dfs(r, c-1) + dfs(r + 1, c) + dfs(r - 1, c)
            return perimeter
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)
        return 0
        