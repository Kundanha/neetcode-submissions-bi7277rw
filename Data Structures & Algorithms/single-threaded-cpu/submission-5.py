class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(n)]
        tasks.sort()

        time = 0
        res = []
        minHeap = []

        i = 0

        while minHeap or i < n:
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]
        
            while i<n and  tasks[i][0] <= time:
                enqtime, processingTime, idx = tasks[i]
                heapq.heappush(minHeap, [processingTime, idx])
                i+=1

            pt, index = heapq.heappop(minHeap)
            time+=pt

            res.append(index)
        return res
        
