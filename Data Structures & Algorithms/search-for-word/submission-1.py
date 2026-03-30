class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def backtrack(r, c, i):
            if len(word) == i:
                return True
            if ((r, c) in path or r not in range(rows) or c not in range(cols) or word[i] != board[r][c]):
                return False
            path.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or
                    backtrack(r - 1, c, i + 1) or
                    backtrack(r, c + 1, i + 1) or
                    backtrack(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
        