class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i, total):
            if total == target:
                res.append(comb.copy())
                return
            if i == len(nums) or total > target:
                return
            comb.append(nums[i])
            backtrack(i, total + nums[i])
            comb.pop()
            backtrack(i+1, total)
        backtrack(0, 0)
        return res
        