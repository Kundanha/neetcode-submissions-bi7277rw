class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)
            if num2 > num1:
                heapq.heappush(stones, num1-num2)
            if num1 == num2:
                continue
        return abs(stones[0]) if stones else 0
        