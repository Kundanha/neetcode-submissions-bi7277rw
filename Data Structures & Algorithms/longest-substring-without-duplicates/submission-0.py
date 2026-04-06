class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = -1
        j = -1
        ans = 0
        while True:
            f1 = False
            f2 = False
            while i<(len(s)-1):
                f1 = True
                i+=1
                mp[s[i]] = mp.get(s[i], 0)+1
                if mp[s[i]] == 2:
                    break
                else:
                    ans = max(ans, (i-j))
            while j<i:
                f2 = True
                j+=1
                mp[s[j]] = mp.get(s[j], 0)-1
                if mp[s[j]] == 1:
                    ans = max(ans, (i-j))
                    break
            if f1 == False and f2 == False:
                break

        return ans


        