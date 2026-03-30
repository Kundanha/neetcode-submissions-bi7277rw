class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(s)
        minHeap = [[-v, k] for k, v in mp.items()]
        heapq.heapify(minHeap)
        res = ""
        prev = None
        while minHeap or prev:
            if prev and not minHeap:
                return ""
            val, key = heapq.heappop(minHeap)
            res+=key
            val+=1
            if prev:
                heapq.heappush(minHeap, prev)
                prev = None
            if val < 0:
                prev = [val, key]
            
        return res

        
        

        