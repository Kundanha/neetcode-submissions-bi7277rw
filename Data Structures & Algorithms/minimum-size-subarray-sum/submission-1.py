class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        res = float("inf")
        total = 0

        for i in range(len(nums)):
            total+=nums[i]
            while total >= target:
                res = min(i-j+1, res)
                total -= nums[j]
                j+=1
        return 0 if res == float("inf") else res
        