import heapq
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Problem: Car pooling possible hai ya nahi?
        # trips[i] = [numPassengers, startLocation, endLocation]
        # Rule: start pe passengers pick up, end pe drop (end is exclusive in effect: at 'end' they leave)
        # Goal: kabhi bhi passengers in car > capacity nahi hone chahiye

        trips.sort(key=lambda t: t[1])
        # Hinglish logic: Trips ko startLocation ke basis pe sort kar diya
        # Taaki hum left-to-right timeline scan kar sakein (jaise events order me handle karte hain)

        minHeap = []
        # minHeap me ongoing trips store karenge as [endLocation, numPassengers]
        # Heap ka top = sabse pehle finish hone wali trip (smallest end)
        # Isse hum quickly drop-offs process kar paate hain

        curPass = 0
        # curPass = current car me kitne passengers hain abhi

        for t in trips:
            # Har trip ko chronological (start ke order) me process kar rahe
            numPass, start, end = t

            while minHeap and minHeap[0][0] <= start:
                # Jab tak koi ongoing trip ka end <= current start
                # matlab wo trip finish ho chuki, passengers drop ho jaayenge
                curPass -= minHeap[0][1]     # passengers remove karo
                heapq.heappop(minHeap)       # trip remove from heap

            curPass += numPass
            # Ab current trip start ho rahi, passengers add karo

            if curPass > capacity:
                # Agar capacity cross ho gayi to immediately false
                return False

            heapq.heappush(minHeap, [end, numPass])
            # Current trip ko ongoing list/heap me add kar diya
            # Future me jab iska end aayega, tab drop karenge

        return True
        # Agar kabhi capacity exceed nahi hui, to possible hai => True


# Time Complexity (kyun?):
# 1) Sorting trips by start: O(n log n)
# 2) Har trip heap me ek baar push hoti hai: n pushes => O(n log n)
# 3) Har trip heap se ek baar pop hoti hai: n pops => O(n log n)
# Total: O(n log n)

# Space Complexity (kyun?):
# Heap worst case me saari trips simultaneously active ho sakti hain => O(n)
# So space: O(n)