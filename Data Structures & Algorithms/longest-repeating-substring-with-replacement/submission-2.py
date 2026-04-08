class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        i = -1
        j = -1
        maxLen = 0
        maxf = 0

        while True:
            l1 = False
            l2 = False
            #aquire
            while i<len(s) - 1:
                i+=1
                hm[s[i]] += 1
                maxf = max(maxf, hm[s[i]])
                windowLen = i-j
                if windowLen - maxf <= k:
                    maxLen = max(maxLen, windowLen)
                else:
                    break
                l1 = True
            #release
            while j < i:
                j+=1
                hm[s[j]] -= 1
                windowLen = i-j
                if windowLen - maxf <= k:
                    maxLen = max(maxLen, windowLen)
                    l2 = True
                    break
            if l1 == False and l2 == False:
                break
        return maxLen



        