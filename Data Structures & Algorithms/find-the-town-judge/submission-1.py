class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for member in trust:
            indegree[member[1]] += 1
            outdegree[member[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1
        