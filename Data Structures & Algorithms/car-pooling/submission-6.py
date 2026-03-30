class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        minHeap = []
        curPass = 0
        for t in trips:
            pas, start, end = t

            while minHeap and minHeap[0][0] <= start:
                e, p = heapq.heappop(minHeap)
                curPass -= p


            curPass += pas

            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, pas]) #car pe baitha liya
        return True
        
        
        