class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPali(s):
            l = 0
            r = len(s) - 1
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r-1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPali(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

        