class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        res = []
        def dfs(u, v, visited):
            if u == v:
                return True
            visited.add(u)
            for nei in adj[u]:
                if nei not in visited: 
                    if dfs(nei, v, visited):
                        return True
            return False
        
        for qu, qv in queries:
            res.append(dfs(qu, qv, set()))
        return res
        