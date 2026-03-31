class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [0] * (len(edges)+1)
        def find(e):
            if e == parent[e]:
                return e
            parent[e] = find(parent[e])
            return parent[e]
        

        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pu] = pv
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []
        