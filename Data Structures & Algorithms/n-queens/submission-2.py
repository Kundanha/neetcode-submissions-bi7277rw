class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdag = set()
        negdag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdag or (r-c) in negdag:
                    continue
                col.add(c)
                posdag.add((r+c))
                negdag.add((r-c))
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                posdag.remove((r+c))
                negdag.remove((r-c))
                board[r][c] = "."
        backtrack(0)
        return res
            
