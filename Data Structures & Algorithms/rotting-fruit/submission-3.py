class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        time = 0

        while q:
            rotten = False
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r in range(rows) and c in range(cols) and (r, c) not in visit and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append([r, c])
                        visit.add((r, c))
                        rotten = True
            if rotten:
                time+=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time