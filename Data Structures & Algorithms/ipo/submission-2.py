from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        IPO Problem (Greedy + Sorting + MaxHeap)

        Hinglish intuition:
        - Tumhare paas initial capital w hai.
        - Tum max k projects kar sakte ho.
        - Har project start karne ke liye minimum capital chahiye (capital[i])
        - Complete karne par profit add hota hai (profits[i]) => w = w + profits[i]

        Goal:
        - Final capital maximize karna after at most k projects.

        Key Greedy idea:
        - Har step pe, jo projects current w se start ho sakte hain (capital <= w),
          unmein se MAX profit wala project choose karo.
          Kyun? Kyunki zyada profit => w jaldi badhega => future me aur projects unlock honge.

        Data structures:
        1) Sort projects by required capital (ascending) => taaki hum pointer se unlock kar sakein.
        2) MaxHeap (profits) => currently unlocked feasible projects me se max profit nikalne ke liye.

        Python me heapq MIN heap hai, so MaxHeap banane ke liye profit ko NEGATIVE store karte hain.
        """

        n = len(profits)

        # Step 1: (capital, profit) pair banao
        projects = [(capital[i], profits[i]) for i in range(n)]

        # Step 2: required capital ke basis pe sort karo
        # Ab projects as per capital: lowest capital required first
        projects.sort(key=lambda x: x[0])

        # maxHeap me hum feasible projects ke profits store karenge (negative values)
        maxHeap = []

        # i pointer => sorted list me abhi tak kitne projects "consider/unlock" ho chuke
        i = 0

        # Step 3: max k times choose karna hai
        # Har iteration:
        #   (a) jitne projects affordable (capital <= w) hain, heap me daalo
        #   (b) heap empty => koi project feasible nahi => break
        #   (c) heap se max profit nikalo => w increase
        for _ in range(k):

            # (a) unlock all feasible projects at current capital w
            # i ko aage badhate raho jab tak capital requirement <= w
            while i < n and projects[i][0] <= w:
                cap_req, prof = projects[i]
                # maxHeap => negative profit push
                heapq.heappush(maxHeap, -prof)
                i += 1

            # (b) agar heap empty hai => koi feasible project available nahi
            # matlab w insufficient hai next locked projects ke liye and no unlocked left
            if not maxHeap:
                break

            # (c) best profit choose karo (max profit)
            best_profit = -heapq.heappop(maxHeap)
            w += best_profit

            # Note:
            # - Project ek baar hi heap me gaya (distinct) and pop hone ke baad "used" ho gaya.

        return w


"""
Time Complexity (Hinglish):
- projects list banane me: O(n)
- sorting: O(n log n)
- har project heap me max 1 baar push hota hai => total pushes <= n, each push O(log n) => O(n log n)
- pop at most k times, each pop O(log n) => O(k log n)

Total:
  O(n log n + k log n)
Since usually k <= n, we say O(n log n).

Space Complexity:
- projects array: O(n)
- heap worst-case: O(n)
Total: O(n)

Why this is optimal (general case):
- Capital values large (up to 1e9), so you can’t bucket-sort easily.
- Greedy step needs “best among feasible” quickly, heap gives that.
- Sorting + heap is standard optimal solution in interviews/LeetCode.
"""