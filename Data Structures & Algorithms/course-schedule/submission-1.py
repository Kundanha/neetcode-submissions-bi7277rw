class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for val in prerequisites:
            a = val[0]
            b = val[1]
            adj[b].append(a)
            indegree[a]+=1
        def toposortcheck():
            q = deque()
            count = 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    count+=1
                    q.append(i)
            while q:
                i = q.popleft()
                for c in adj[i]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)
                        count+=1
            if count == numCourses:
                return True
            return False
        return toposortcheck()

