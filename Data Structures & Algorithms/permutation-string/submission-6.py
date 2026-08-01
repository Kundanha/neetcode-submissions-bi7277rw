class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = -1
        j = -1
        hm = Counter(s1)
        count = len(hm)
        k = len(s1)

        while True:
            l1 = False
            l2 = False
            while i < len(s2)-1 and i - j < k:
                i+=1
                ch = s2[i]
                if ch in hm:
                    hm[ch] -= 1
                    if hm[ch] == 0:
                        count-=1
                l1 = True
            while j < i and i - j == k:
                if count == 0:
                    return True
                j+=1
                ch = s2[j]
                if ch in hm:
                    if hm[ch] == 0:
                        count+=1
                    hm[ch] += 1
                l2 = True
                break
            if l1 == False and l2 == False:
                break
        return False
        