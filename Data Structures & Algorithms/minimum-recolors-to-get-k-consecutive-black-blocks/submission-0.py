class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = -1
        j = -1
        wcount = 0
        ans = float("inf")
        while True:
            l1 = False
            l2 = False

            while i < len(blocks) - 1 and (i - j) < k:
                i+=1
                if blocks[i] == "W":
                    wcount+=1
                l1 = True
            while j < i and (i - j) == k:
                if i - j == k:
                    ans = min(ans, wcount)
                j+=1
                if blocks[j] == "W":
                    wcount-=1
                l2 = True
                break
            if not l1 and not l2:
                break
        return ans

        