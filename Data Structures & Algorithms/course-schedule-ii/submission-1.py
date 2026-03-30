class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        res = []
        def bfs():
            q = deque()
            count = 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
                    res.append(i)
                    count+=1
            
            while q:
                crs = q.popleft()
                for c in adj[crs]:
                    indegree[c]-=1
                    if indegree[c] == 0:
                        q.append(c)
                        res.append(c)
                        count+=1
            if count == numCourses:
                return res
            return []
        return bfs()


        