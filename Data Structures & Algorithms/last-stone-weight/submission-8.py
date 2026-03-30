class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one < two:
                sub = one - two
                heapq.heappush(stones, sub)
        return abs(stones[0]) if stones else 0
        