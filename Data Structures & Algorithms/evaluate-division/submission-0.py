class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            e1 = equations[i][0]
            e2 = equations[i][1]
            val = values[i]
            adj[e1].append((e2, val))
            adj[e2].append((e1, 1 / val))
        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1
            visited.add(src)
            for nei, val in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return val * result
            return -1
        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res

        