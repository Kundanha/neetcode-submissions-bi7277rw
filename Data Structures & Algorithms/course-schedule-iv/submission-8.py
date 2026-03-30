class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        isPre = [set() for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                isPre[nei].add(node)
                isPre[nei].update(isPre[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return [u in isPre[v] for u, v in queries]

        