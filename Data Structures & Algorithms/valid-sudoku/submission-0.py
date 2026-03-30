class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        squset = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowset[i] or board[i][j] in colset[j] or board[i][j] in squset[(i//3, j//3)]):
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                squset[(i//3, j//3)].add(board[i][j])
        return True

        