from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Alternate Approach 1: Sweep Line / Difference Array (Event Counting)
        ---------------------------------------------------------------
        Idea (Hinglish + English):
        - Har trip me:
          start pe passengers +numPass add hote hain
          end pe passengers -numPass remove hote hain
        - Hum "events" bana lete hain: delta[start] += numPass, delta[end] -= numPass
        - Phir left-to-right accumulate karke check karte hain ki capacity cross to nahi ho rahi.

        Why it works:
        - Ye exact wahi simulate karta hai jo car me hota hai: pick-up at start, drop at end.
        - Order matters: end point pe drop ho jata hai before next pickup at same point,
          but delta method naturally handle karta hai because we apply deltas at that location.

        Time Complexity:
        - If location range bounded (LeetCode me typically 0..1000): O(R + n), R = max location range
        - Otherwise, if coordinates large: you can compress coordinates (see approach 2)

        Space Complexity:
        - O(R) for delta array (or O(unique_points) with map version)
        """

        # LeetCode constraints version: locations 0..1000
        # Agar range unknown ho, toh maxEnd nikaal ke array size set kar do
        maxEnd = 0
        for numPass, start, end in trips:
            if end > maxEnd:
                maxEnd = end

        delta = [0] * (maxEnd + 1)
        # delta[x] = net change in passengers at location x

        for numPass, start, end in trips:
            delta[start] += numPass  # pickup
            delta[end] -= numPass    # drop

        cur = 0
        for x in range(maxEnd + 1):
            cur += delta[x]
            if cur > capacity:
                return False

        return True