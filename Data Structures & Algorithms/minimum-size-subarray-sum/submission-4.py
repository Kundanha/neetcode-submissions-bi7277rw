class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        total = 0
        minimal = float("inf")

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minimal = min(minimal, i - j +1)
                total -= nums[j]
                j += 1
        return 0 if minimal == float("inf") else minimal

        