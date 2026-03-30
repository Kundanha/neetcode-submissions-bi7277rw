class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(par))
                return
            if openN < n:
                par.append("(")
                dfs(openN + 1, closeN)
                par.pop()
            if closeN < openN:
                par.append(")")
                dfs(openN, closeN + 1)
                par.pop()
        dfs(0, 0)
        return res
        