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
        for sub in res:
            x = 0
            for s in sub:
                x^=s
            total+=x
        return total

            
            

        