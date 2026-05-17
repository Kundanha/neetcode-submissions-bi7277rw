class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r, c) not in visit:
                        grid[r][c] = dist + 1
                        q.append([r, c])
                        visit.add((r, c))
            dist+=1