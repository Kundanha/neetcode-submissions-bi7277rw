class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        def find(e):
            if e == parents[e]:
                return e
            return find(parents[e])
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            parents[pa] = pb
            return True
        res = n
        for u, v in edges:
            if union(u, v):
                res-=1
        return res

        