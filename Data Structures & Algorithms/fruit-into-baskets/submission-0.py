class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = -1
        j = -1
        typefruit = defaultdict(int)
        res = 0

        while True:
            l1 = False
            l2 = False

            while i < len(fruits) -1:
                i+=1
                typefruit[fruits[i]] +=1
                l1 = True
                if len(typefruit) <= 2:
                    res = max(res, i - j)
                else:
                    break
            while j < i:
                j+=1
                typefruit[fruits[j]] -=1
                l2 = True
                if typefruit[fruits[j]] == 0:
                    del typefruit[fruits[j]]
                
                if len(typefruit) <= 2:
                    res = max(res, i - j)
                    break
            if not l1 and not l2:
                break
        return res

                
                
