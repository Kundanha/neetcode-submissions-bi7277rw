class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(root, visited):
            visited.add(root)
            h = 0
            q = deque([root])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                h+=1
            return h
        height = float("inf")
        res = []
        for i in range(n):
            h = bfs(i, set())
            if height > h:
                height = h
                res = [i]
            elif height == h:
                res.append(i)
        return res


