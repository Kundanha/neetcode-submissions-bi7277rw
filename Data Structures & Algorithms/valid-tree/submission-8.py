class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = [i for i in range(n)]

        def find(e):
            if e == parent[e]:
                return e
            parent[e] = find(parent[e])
            return parent[e]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            parent[pa] = pb
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        return True
        