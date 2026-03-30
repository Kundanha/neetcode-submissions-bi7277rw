class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse = True)
        target = sum(nums)//k
        used = [False] * len(nums)

        def dfs(i, k, sub):
            if k == 0:
                return True
            if sub == target:
                return dfs(0, k-1, 0)
            for j in range(i, len(nums)):
                if used[j] or sub + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, sub + nums[j]):
                    return True
                used[j] = False
            return False
        return dfs(0, k, 0)
        