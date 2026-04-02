class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        res = []
        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        while n > 2:
            size = len(q)
            n-=size
            for _ in range(size):
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        while q:
            res.append(q.popleft())
        return res

        