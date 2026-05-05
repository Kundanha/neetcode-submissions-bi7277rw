class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                directions = [[1, 0], [0, 1], [-1, 0], [ 0, -1]]
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r not in range(rows) or c not in range(cols) or  grid[r][c] == -1 or (r, c) in visited:
                        continue
                    q.append((r, c))
                    visited.add((r, c))
            dist+=1
