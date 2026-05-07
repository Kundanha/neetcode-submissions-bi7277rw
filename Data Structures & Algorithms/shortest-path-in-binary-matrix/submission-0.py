class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        pq = [[0, 0, 0]]
        heapq.heapify(pq)
        n = len(grid)
        if n == 0 or grid[0][0] == 1:
            return -1
        res = [[float("inf")] * n for _ in range(n)]
        
        res[0][0] = 0
        while pq:
            d, row, col = heapq.heappop(pq)
            if row == n-1 and col == n-1:
                return d+1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]
            for rd, cd in directions:
                r = rd + row
                c = cd + col
                if r in range(n) and c in range(n) and grid[r][c] == 0:
                    if d+1 < res[r][c]:
                        res[r][c] = d+1
                        heapq.heappush(pq, [d + 1, r, c])
        return -1

