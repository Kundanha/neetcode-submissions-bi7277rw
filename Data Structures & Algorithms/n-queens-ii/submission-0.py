class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0]
        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                res[0] += 1
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
        backtrack(0)
        return res[0]


        