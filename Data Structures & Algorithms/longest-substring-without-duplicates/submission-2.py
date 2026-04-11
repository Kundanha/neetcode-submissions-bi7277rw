class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        left = 0
        longest = 0

        for right in range(len(s)):
                if s[right] in hm:
                        left = max(left, hm[s[right]]+1)
                hm[s[right]] = right
                longest = max(longest, right - left + 1)
        return longest