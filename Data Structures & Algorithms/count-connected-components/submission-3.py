class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [0] * n
        def find(e):
            if e == parents[e]:
                return e
            parents[e] = find(parents[e])
            return parents[e]
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if rank[pa] > rank[pb]:
                parents[pa] = pb
            elif rank[pa] < rank[pb]:
                parents[pb] = pa
            else:
                parents[pa] = pb
            return True
        res = n
        for u, v in edges:
            if union(u, v):
                res-=1
        return res

        