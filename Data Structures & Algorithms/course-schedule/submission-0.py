class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for val in prerequisites:
            a = val[0]
            b = val[1]
            adj[a].append(b)
        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if adj[c] == []:
                return True

            visit.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        