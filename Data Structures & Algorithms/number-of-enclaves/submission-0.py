class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    q.append([r, c])
                    visit.add((r, c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for rd, cd in directions:
                r = row + rd
                c = col + cd
                if r in range(rows) and c in range(cols) and grid[r][c] == 1  and (r, c) not in visit:
                    q.append([r, c])
                    visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res+=1
        return res

