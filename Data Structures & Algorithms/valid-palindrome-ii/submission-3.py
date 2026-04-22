class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count = 0
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        while l < r:
            if s[l] != s[r]:
                if isPali(l+1, r):
                    return True
                elif isPali(l, r-1):
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True

                
        