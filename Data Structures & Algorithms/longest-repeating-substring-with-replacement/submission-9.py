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
            while i < len(s) - 1:
                i+=1
                hm[s[i]] += 1
                maxf = max(maxf, hm[s[i]])
                window = i - j
                l1 = True
                if window - maxf <= k:
                    maxLen = max(maxLen, window)
                else:
                    break
            while j < i:
                j+=1
                hm[s[j]] -= 1
                window = i - j
                l2 = True
                maxf = max(maxf, hm[s[j]])
                if window - maxf <= k:
                    maxLen = max(maxLen, window)
                    break
            if not l1 and not l2:
                break
         return maxLen

        