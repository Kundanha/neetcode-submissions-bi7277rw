class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def bfs(r, c):
            visited.add((r, c))

            q = deque()
            q.append((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            perimeter = 0
            while q:
                r, c = q.popleft()
                for rd, cd in directions:
                    row = r + rd
                    col = c + cd
                    if row not in range(rows) or col not in range(cols) or grid[row][col] == 0:
                        perimeter+=1
                    elif (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
            return perimeter
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return bfs(r, c)
        return 0


        
        