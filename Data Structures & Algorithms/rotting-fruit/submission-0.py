class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        while q:
            fresh = False
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visit):
                        grid[row][col] = 2
                        q.append([row, col])
                        visit.add((row, col))
                        fresh = True
            if fresh:
                minutes += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes

        
        

        