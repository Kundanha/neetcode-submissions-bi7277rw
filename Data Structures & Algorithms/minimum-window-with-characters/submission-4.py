class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapt = Counter(t)
        dupmatchcount = len(t)
        maps = defaultdict(int)
        i = -1
        j = -1
        ans = ""
        matchcount = 0

        while True:
            l1 = False
            l2 = False
            while i < len(s) - 1 and matchcount < dupmatchcount:
                i+=1
                maps[s[i]] += 1
                if maps[s[i]] <= mapt[s[i]]:
                    matchcount+=1
                l1 = True
            while j < i and matchcount == dupmatchcount:
                potentialAns = s[j+1: i+1]
                if ans == "" or len(ans) > len(potentialAns):
                    ans = potentialAns
                j+=1
                maps[s[j]] -= 1
                if maps[s[j]] < mapt[s[j]]:
                    matchcount-=1
                l2 = True
            if not l1 and not l2:
                break
        return ans
                
                
        