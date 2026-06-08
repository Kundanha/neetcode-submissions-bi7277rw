class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(par))
                return
            if openN < n:
                par.append("(")
                backtrack(openN+1, closeN)
                par.pop()
            if closeN < openN:
                par.append(")")
                backtrack(openN, closeN+1)
                par.pop()
        backtrack(0, 0)
        return res
                
        