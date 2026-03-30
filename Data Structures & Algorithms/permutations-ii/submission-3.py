class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        pick = [False] * len(nums)

        def dfs():
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if pick[i]:
                    continue
                if i and nums[i] == nums[i - 1] and not pick[i - 1]:
                    continue
                pick[i] = True
                perm.append(nums[i])
                dfs()
                perm.pop()
                pick[i] = False
        nums.sort()
        dfs()
        return res
        