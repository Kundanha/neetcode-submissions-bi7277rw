class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(s)
        heap = [[-v, k] for k, v in mp.items()]

        heapq.heapify(heap)

        res = ""
        prev = None

        while heap or prev:
            if not heap and prev:
                return ""
            
            val, key = heapq.heappop(heap)

            res+=key
            val+=1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if val < 0:
                prev = [val, key]
        return res
        