from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Alternate Approach 2: Event Map + Sorting (when locations are large)
        -------------------------------------------------------------------
        Idea:
        - Difference array same, but array size huge ho sakta hai.
        - So use hashmap/dict: events[pos] += passengersChange
        - Then sort all unique positions and accumulate.

        Key detail:
        - At same position, drops and pickups both happen.
        - Using net delta at that position is fine because drop is encoded as negative.
          (Essentially end is "drop at end" and start is "pickup at start".)

        Time Complexity:
        - Build events: O(n)
        - Sort unique points: O(m log m), m <= 2n
        - Sweep: O(m)
        => Total: O(n log n)

        Space Complexity:
        - O(m) for events dict
        """

        events = defaultdict(int)

        for numPass, start, end in trips:
            events[start] += numPass   # pickup
            events[end] -= numPass     # drop

        cur = 0
        for pos in sorted(events):
            cur += events[pos]
            if cur > capacity:
                return False

        return True