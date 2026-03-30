class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posd = set()
        negd = set()
        res = [0]

        def backtrack(r):
            if r == n:
                res[0] += 1
                return
            for c in range(n):
                if c in col or (r+c) in posd or (r-c) in negd:
                    continue
                col.add(c)
                posd.add((r+c))
                negd.add((r-c))
                backtrack(r+1)
                col.remove(c)
                posd.remove((r+c))
                negd.remove((r-c))
        backtrack(0)
        return res[0]
