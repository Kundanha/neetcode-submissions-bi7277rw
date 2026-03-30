class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1: return True # Edge case: single node
        adj = defaultdict(list)
        degree = [0]* n
        for i, j in edges:
            adj[j].append(i)
            adj[i].append(j)
            degree[i]+=1
            degree[j]+=1

        def validTree():
            q = deque()
            count = 0
            for i in range(n):
                if degree[i] == 1:
                    q.append(i)
            while q:
                node = q.popleft()
                count+=1
                for a in adj[node]:
                    degree[a]-=1
                    if degree[a] == 1:
                        q.append(a)
            return count == n
        return validTree()
        