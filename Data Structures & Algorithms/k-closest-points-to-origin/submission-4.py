class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distpoints = [[(math.sqrt(((x - 0)**2 )+ ((y - 0)**2))), x, y] for x, y in points]
        heapq.heapify(distpoints)
        res = []
        while k:
            dist, x, y = heapq.heappop(distpoints)
            res.append([x, y])
            k-=1
        return res

        