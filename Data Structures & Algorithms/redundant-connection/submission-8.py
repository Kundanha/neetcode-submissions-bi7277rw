class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        #visited = set()

        def dfs(u, v, visited):
            visited.add((u, v))

            if u == v:
                return True
            for nei in adj[u]:
                if (nei, v) not in visited:
                    if dfs(nei, v, visited):
                        return True
            return False

        for u, v in edges:
            if u in adj and v in adj and dfs(u, v, set()):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)
        return []