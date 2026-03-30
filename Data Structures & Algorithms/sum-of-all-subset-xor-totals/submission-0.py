class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        sub = []

        def backtrack(i):
            if i == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)
        backtrack(0)
        total = 0
        for l in res:
            x = 0
            if l and len(l) > 1:
                for e in l:
                    x ^=e
                total+= x
            elif l and len(l) == 1:
                total+=l[0]
        return total
        