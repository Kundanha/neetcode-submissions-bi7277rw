from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1) Har task ki frequency count karo
        mp = Counter(tasks)

        # 2) Max-heap chahiye, but Python me min-heap hota hai
        #    Isliye frequencies ko negative karke heap banate hain
        pq = [-cnt for cnt in mp.values()]
        heapq.heapify(pq)

        time = 0  # total time units (tasks + idle)

        # 3) Jab tak heap me tasks pending hain
        while pq:
            temp = []  # is cycle (window) me jo tasks use hue, unki updated freq yaha store hogi

            # 4) Ek window ki length = (n + 1)
            #    Reason: same task ko repeat karne se pehle n cooldown gap ensure karna hota hai
            for _ in range(n + 1):
                if pq:
                    top = heapq.heappop(pq)  # most frequent task (negative value)
                    top += 1                 # ek execution hua => negative freq 1 step zero ki taraf move karegi
                    temp.append(top)         # is task ki remaining freq baad me push karenge (agar abhi bhi pending ho)
                # else: heap empty => is slot me kuch task available nahi, later idle consider ho sakta

            # 5) Jo tasks abhi bhi pending hain (freq < 0), unko wapas heap me daalo
            for t in temp:
                if t < 0:
                    heapq.heappush(pq, t)

            # 6) Time update logic (yehi “last part” hai):
            #    - Agar pq empty ho gaya => sab tasks finish, last window me idle add karne ki need nahi
            #      so actual executed tasks = len(temp) (jitne pop kiye)
            #    - Agar pq empty nahi => abhi tasks bache hain, to window full length (n+1) count hogi
            #      even if kuch slots idle the
            if not pq:
                time += len(temp)
            else:
                time += (n + 1)

        return time