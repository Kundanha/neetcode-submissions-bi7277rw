class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        island = deque()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return
            island.append((r, c))
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        found = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        res= 0
        while island:
            for _ in range(len(island)):
                row, col = island.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r in range(rows) and c in range(cols) and (r, c) not in visited:
                        if grid[r][c] == 0:
                            island.append((r, c))
                            visited.add((r, c))
                        else:
                            return res
            res+=1




