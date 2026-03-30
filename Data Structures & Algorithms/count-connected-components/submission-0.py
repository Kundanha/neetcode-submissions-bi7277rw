class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        return res
        