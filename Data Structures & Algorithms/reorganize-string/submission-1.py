import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Problem: Adjacent same characters nahi hone chahiye.
        # Idea: Greedy + MaxHeap (Python me maxheap banane ke liye negative counts use karte hain)

        mp = Counter(s)  
        # mp = har character ki frequency map
        # Example: "aaabbc" -> {'a':3,'b':2,'c':1}

        minHeap = [[-v, k] for k, v in mp.items()]
        # Heap me store kar rahe: [-count, char]
        # -count isliye kyunki heapq min-heap hai, hume max freq wala char pehle chahiye

        heapq.heapify(minHeap)
        # Ab heap ready hai: top pe hamesha most frequent char aayega (because most negative)

        res = ""
        # Final answer string yaha build hogi

        prev = None
        # prev = last used character ko temporarily hold karega
        # reason: same char ko immediately wapas heap me daal doge to next pop me wahi aa sakta hai
        # so ek step delay karte hain

        while minHeap or prev:
            # Loop tab tak chalayenge jab tak heap me kuch bacha ho ya prev pending ho

            if prev and not minHeap:
                # Agar prev pending hai but heap empty ho gaya
                # matlab next different char available hi nahi hai => arrangement impossible
                return ""

            val, key = heapq.heappop(minHeap)
            # Heap se most frequent char nikala
            # val negative hai, key character hai

            res += key
            # Answer me current char append kar diya

            val += 1
            # Kyunki val negative hai:
            # e.g. val = -3, ek use kiya => -2 (so +1)
            # matlab frequency decrease ho gayi

            if prev:
                # Pichla character jo hold karke rakha tha, ab safe hai heap me wapas daalna
                # Kyunki ab humne ek different char place kar diya
                heapq.heappush(minHeap, prev)
                prev = None

            if val < 0:
                # Agar current char ab bhi remaining hai (freq still > 0)
                # to isko prev me hold karo, taaki next turn me repeat na ho
                prev = [val, key]

        return res
        # res will be valid if possible, else we returned "" earlier