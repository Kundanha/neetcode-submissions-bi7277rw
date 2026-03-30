class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        res = []
        pes = set()
        atl = set()
        def dfs(r, c, visit, preHeight):
            if ((r, c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < preHeight):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pes, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pes, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pes and (r, c) in atl:
                    res.append([r, c])
        return res

        