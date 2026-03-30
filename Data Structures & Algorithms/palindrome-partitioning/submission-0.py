class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substr = []
        def isPali(s):
            l = 0
            r = len(s) - 1
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(substr.copy())
                return
            if isPali(s[j:i+1]):
                substr.append(s[j:i+1])
                dfs(i+1, i+1)
                substr.pop()
            dfs(j , i + 1)
            return res
        dfs(0, 0)
        return (res)

        