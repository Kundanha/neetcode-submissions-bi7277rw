class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)
            if num2 > num1:
                diff = num1-num2
                heapq.heappush(stones, diff)
        stones.append(0)
        print(stones)
        return abs(stones[0])