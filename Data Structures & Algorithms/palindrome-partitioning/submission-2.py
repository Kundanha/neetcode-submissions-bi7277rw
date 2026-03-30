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
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if isPali(s[j:i+1]):
                part.append(s[j:i+1])
                dfs(i+1, i+1)
                part.pop()
            dfs(j, i+1)
        dfs(0, 0)
        return res

        