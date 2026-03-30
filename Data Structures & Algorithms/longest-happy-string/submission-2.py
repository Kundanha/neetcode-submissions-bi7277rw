class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        maxHeap = [[-count, char] for count, char in [[a, "a"], [b, "b"], [c, "c"]] if count > 0]
        heapq.heapify(maxHeap)

        res = ""

        while maxHeap:

            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2 +=1
                res += char2

                if count2:
                    heapq.heappush(maxHeap, [count2, char2])
                heapq.heappush(maxHeap, [count, char])
            else:
                count+=1
                res+=char
                if count:
                    heapq.heappush(maxHeap, [count, char])
        return res

        