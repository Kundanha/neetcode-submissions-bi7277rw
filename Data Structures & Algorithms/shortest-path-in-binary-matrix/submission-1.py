class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        if n == 1:
            return 1
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        q.append((0, 0))
        count = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]
                for rd, cd in directions:
                    r = rd + row
                    c = cd + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == 0:
                        if r == rows-1 and c == rows-1:
                            return count + 1
                        grid[r][c] = 1
                        q.append((r, c))
            count+=1
        return -1

