class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rowCount = [0] * rows
        colCount = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1
        server = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rowCount[r] > 1 or colCount[c] > 1:
                        server += 1
        return server