class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capProf = [[capital[i], profits[i]] for i in range(len(capital))]
        capProf.sort()
        maxHeap = []
        i = 0

        while k > 0:
            while i< len(capProf) and capProf[i][0] <= w:
                heapq.heappush(maxHeap, -capProf[i][1])
                i+=1
            if not maxHeap:
                break
            prof = -heapq.heappop(maxHeap)
            w+=prof
            k-=1
           
        return w


        