class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        projects = [[capital[i], profits[i]] for i in range(n)]
        projects.sort(key=lambda x: x[0])
        maxHeap = []

        i = 0


        for _ in range(k):

            while i<n and projects[i][0] <= w:
                cap, prof = projects[i]
                heapq.heappush(maxHeap, -prof)
                i += 1
            
            if not maxHeap:
                break
            
            best_profit = -heapq.heappop(maxHeap)
            w+=best_profit
        return w
            
        