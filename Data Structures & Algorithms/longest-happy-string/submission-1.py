import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Problem: "happy string" banana hai using 'a','b','c'
        # Constraint: kisi bhi character ka "aaa" / "bbb" / "ccc" (3 in a row) allowed nahi.
        # Goal: string as long as possible.

        res = ""
        # res = answer string jo hum build karenge

        maxHeap = [(-count, char) for count, char in [(a, "a"), (b, "b"), (c, "c")] if count > 0]
        # Heap me (negativeCount, char) store kar rahe
        # Negative isliye kyunki heapq min-heap hai, hume max freq wala char pehle chahiye
        # Sirf wahi chars push karo jinka count > 0 hai

        heapq.heapify(maxHeap)
        # Ab heap ready: top pe most available char aayega

        while maxHeap:
            # Jab tak heap me kuch available hai tab tak build karte raho

            count, char = heapq.heappop(maxHeap)
            # Most frequent char pop kiya
            # count negative hai (e.g. -5 means 5 remaining)

            if len(res) > 1 and res[-1] == res[-2] == char:
                # Agar last two chars same hain aur hum same char add karenge
                # to 3 in a row ban jayega => NOT allowed

                if not maxHeap:
                    # Agar alternate char available hi nahi hai
                    # matlab aur extend possible nahi, break
                    break

                count2, char2 = heapq.heappop(maxHeap)
                # Next best (second most frequent) char nikaal liya
                # Isko use karenge taaki constraint break na ho

                count2 += 1
                # Kyunki count2 negative hai:
                # ek char use kiya => remaining reduce => -k becomes -(k-1) => +1

                res += char2
                # Safe char add kar diya

                if count2:
                    # Agar char2 ab bhi remaining hai (count2 != 0)
                    # to heap me wapas push karo
                    heapq.heappush(maxHeap, (count2, char2))

                # Ab jo original char (char) ko hum use nahi kar paaye the,
                # usko bhi wapas heap me daal do for future tries
                heapq.heappush(maxHeap, (count, char))

            else:
                # Safe case: last two chars same nahi hain
                # to hum top char directly add kar sakte hain

                res += char
                # char add kar diya

                count += 1
                # ek use kiya => remaining reduce (negative count + 1)

                if count:
                    # Agar char ab bhi remaining hai (count != 0)
                    # to heap me wapas daal do
                    heapq.heappush(maxHeap, (count, char))

        return res
        # res will be longest possible happy string by this greedy approach