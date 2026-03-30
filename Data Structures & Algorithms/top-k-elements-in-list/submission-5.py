class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        sortedhm = {k: v for k, v in sorted(hm.items(), key=lambda item: item[1], reverse=True)}
        res = []
        i = 0
        print(sortedhm)
        while k:
            res.append(list(sortedhm.keys())[i])
            i+=1
            k-=1
        return res


        