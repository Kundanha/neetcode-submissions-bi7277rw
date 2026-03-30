class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        pq = [-i for i in mp.values()]
        heapq.heapify(pq)
        time = 0


        while pq:
            temp = []
            for i in range(n+1):
                if pq:
                    top = heapq.heappop(pq)
                    top+=1
                    temp.append(top)
            for t in temp:
                if t<0:
                    heapq.heappush(pq, t)
            if not pq:
                time += len(temp)
            else:
                time += n+1
        return time
            

        