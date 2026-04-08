class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = -1
        j = -1
        longest = 0
        mp = defaultdict(int)
        while True:
            l1 = False
            l2 = False
            while i<len(s)-1:
                i+=1
                mp[s[i]] += 1
                l1 = True
                if mp[s[i]] == 2:
                    break
                else:
                    longest = max(longest, i-j)
            while j < i:
                j+=1
                mp[s[j]] -= 1
                l2 = True
                if mp[s[j]] == 1:
                    longest = max(longest, i-j)
                    break
            if l1 == False and l2 == False:
                break
        return longest

                

        