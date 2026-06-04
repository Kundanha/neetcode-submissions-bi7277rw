class Solution:
    def scoreOfString(self, s: str) -> int:
        l = len(s) - 2
        r = len(s) - 1
        res = 0

        while l >= 0:
            res+= abs(ord(s[r]) - ord(s[l]))
            l-=1
            r-=1
        return res
        