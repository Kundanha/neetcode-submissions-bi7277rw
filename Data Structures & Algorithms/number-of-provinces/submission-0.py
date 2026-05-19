class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()
        res = 0
        for i in range(n):
            if i not in visit:
                q = deque()
                res+=1
                q.append(i)
                visit.add(i)

                while q:
                    i = q.popleft()
                    for j in range(n):
                        if isConnected[i][j] and j not in visit:
                            q.append(j)
                            visit.add(j)
        return res


        


        
        