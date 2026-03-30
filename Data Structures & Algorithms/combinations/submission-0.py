class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            if i > n:
                if len(sub) == k:
                    res.append(sub.copy())
                return
            sub.append(i)
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(1)
        return res
            