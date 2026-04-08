class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        for i in range(len(s)):
            freq = [0] * 26
            maxf = 0
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord("A")] += 1
                maxf = max(maxf, freq[ord(s[j]) - ord("A")])
                changes = (j-i+1) - maxf
                if changes <= k:
                    maxlen = max(maxlen, (j-i+1))
                else:
                    break
        return maxlen


        