class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        pq = [-i for i in mp.values()]
        heapq.heapify(pq)

        time = 0

        while pq:
            stack = []

            for i in range(n+1):
                if pq:
                    t = heapq.heappop(pq)
                    t+=1
                    stack.append(t)
            for s in stack:
                if s<0:
                    heapq.heappush(pq, s)

            if not pq:
                time+=len(stack)
            else:
                time+=(n+1)
        return time
