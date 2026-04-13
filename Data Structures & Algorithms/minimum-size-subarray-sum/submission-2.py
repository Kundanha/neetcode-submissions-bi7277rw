class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = -1
        j = -1
        minimal = float("inf")

        total = 0

        while True:
            l1 = False
            l2 = False

            while i < len(nums) - 1 and total < target:
                i+=1
                total += nums[i]
                l1 = True
            while j < i and total >= target:
                minimal = min(minimal, i - j)
                j += 1
                total -= nums[j]
                l2  = True
            if not l1 and not l2:
                break
        return 0 if minimal == float("inf") else minimal