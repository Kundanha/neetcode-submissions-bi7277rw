class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = -1
        j = -1
        longest = 0
        hm = defaultdict(int)

        while True:
            l1 = False
            l2 = False

            while i < len(s) - 1:
                i +=1
                hm[s[i]] +=1
                l1 = True
                if hm[s[i]] == 2:
                    break
                else:
                    longest = max(longest, i - j)
            while j < i:
                j+=1
                hm[s[j]] -= 1
                l2 = True
                if hm[s[j]] == 1:
                    longest = max(longest, i-j)
                    break
            if not l1 and not l2:
                break
        return longest