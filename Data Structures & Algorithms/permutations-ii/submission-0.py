class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        pick = [False] * len(nums)

        def dfs():
            if len(nums) == len(perm):
                if perm not in res:
                    res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perm.append(nums[i])
                    dfs()
                    perm.pop()
                    pick[i] = False
        dfs()
        return res
        