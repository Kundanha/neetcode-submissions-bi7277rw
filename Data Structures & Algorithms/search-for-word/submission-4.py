class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            res = backtrack(r - 1, c, i + 1) or backtrack(r + 1, c, i + 1) or backtrack(r, c - 1, i + 1) or backtrack(r, c + 1, i + 1)
            visited.remove((r, c))
            return res



        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
        