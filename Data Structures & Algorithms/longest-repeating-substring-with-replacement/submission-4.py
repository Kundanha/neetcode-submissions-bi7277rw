class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = -1
        j = -1
        maxf = 0
        maxLen = 0
        hm = defaultdict(int)
        while True:
            l1 = False
            l2 = False
            while i < len(s)-1:
                l1 = True
                i+=1
                hm[s[i]] += 1
                maxf = max(maxf, hm[s[i]])
                windowLen = i - j
                if windowLen - maxf <= k:
                    maxLen = max(maxLen, windowLen)
                else:
                    break
            while j < i:
                l2 = True
                j+=1
                hm[s[j]] -= 1
                windowLen = i - j
                if windowLen - maxf <= k:
                    maxLen = max(maxLen, windowLen)
                    break
            if l1 == False and l2 == False:
                break
        return maxLen

                

        