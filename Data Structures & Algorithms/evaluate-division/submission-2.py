class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            e1 = equations[i][0]
            e2 = equations[i][1]
            val = values[i]
            adj[e1].append((e2, val))
            adj[e2].append((e1, 1/val))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque([(src, 1)])
            visit = set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1
        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        return res

        