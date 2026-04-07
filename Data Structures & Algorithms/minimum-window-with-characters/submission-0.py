class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map2 = Counter(t)
        i = -1
        j = -1
        map1 = defaultdict(int)
        mct = 0
        dmct = len(t)
        ans = ""
        while True:
            l1 = False
            l2 = False
            #aquaire
            while i< len(s)-1 and mct < dmct:
                i+=1
                map1[s[i]] += 1
                if map1[s[i]] <= map2[s[i]]:
                    mct+=1
                l1 = True
            #collect ans and release
            while j < i and mct == dmct:
                potentialAns = s[j+1: i+1]
                if len(ans) == 0 or len(potentialAns) < len(ans):
                    ans = potentialAns
                j+=1
                if map1[s[j]] == 1:
                    map1.pop(s[j])
                else:
                    map1[s[j]] -= 1
                if map1.get(s[j], 0) < map2[s[j]]:
                    mct-=1
                l2 = True
            if l1 == False and l2 == False:
                break
        return ans
                
