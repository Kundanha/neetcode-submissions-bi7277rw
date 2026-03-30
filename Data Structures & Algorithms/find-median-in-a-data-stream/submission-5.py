import heapq

class MedianFinder:
    """
    Two-Heap approach:
    - left (maxHeap): chhote half numbers, top pe left half ka maximum
    - right (minHeap): bade half numbers, top pe right half ka minimum

    Python me maxHeap directly nahi hota, so hum values ko NEGATIVE karke store karte hain.
    Example: left me -5 store kiya matlab actual value 5 hai.
    """

    def __init__(self):
        # left = maxHeap (store negatives)
        self.left = []
        # right = minHeap (store positives)
        self.right = []

    def addNum(self, num: int) -> None:
        """
        Goal:
        1) left aur right ka size difference max 1 rahe
        2) left ke saare elements <= right ke saare elements
        3) (convention) left ko equal ya 1 extra element rakhenge
        """

        # Step 1: num ko pehle left (maxHeap) me daal do
        # left maxHeap hai (negatives), so -num push karenge
        heapq.heappush(self.left, -num)

        # Step 2: order maintain karne ke liye left ka largest element right me shift kar do
        # left ka largest = -self.left[0] (because negative)
        largest_left = -heapq.heappop(self.left)
        heapq.heappush(self.right, largest_left)

        # Ab possible hai right me zyada elements aa gaye hon,
        # Step 3: balance sizes: agar right > left, right ka smallest wapas left me daal do
        if len(self.right) > len(self.left):
            smallest_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -smallest_right)

        # Invariants (hamesha true hone chahiye):
        # - len(left) == len(right)  OR  len(left) == len(right)+1
        # - max(left) <= min(right)
        # Median nikalna easy ho jaata hai tops se.

    def findMedian(self) -> float:
        """
        Median logic:
        - Agar total elements odd hain: left me 1 extra hoga, so median = top of left
        - Agar even hain: median = (top of left + top of right) / 2
        """

        # left top actual value = -self.left[0]
        if len(self.left) > len(self.right):
            return float(-self.left[0])

        # even case: left aur right same size
        return (-self.left[0] + self.right[0]) / 2.0


# -------------------------
# Quick dry-run (Hinglish)
# -------------------------
# add 1:
# left push -1, shift to right => right=[1], balance => left=[-1], right=[]
# median = 1
#
# add 3:
# left push -3 => left=[-3,-1], shift max(3) to right => right=[3], left=[-1]
# balance ok (sizes equal), median = (1+3)/2=2
#
# add 2:
# left push -2 => left=[-2,-1], shift max(2) to right => right=[2,3], left=[-1]
# balance (right>left) => move 2 back to left => left=[-2,-1], right=[3]
# median = 2