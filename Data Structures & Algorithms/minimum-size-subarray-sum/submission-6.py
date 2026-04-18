class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = -1
        j = -1
        size = float("inf")
        total = 0
        while True:
            l1 = False
            l2 = False

            while i  < len(nums) - 1:
                i += 1
                total += nums[i]
                l1 = True
                if total >= target:
                    break
            while j < i:
                if total >= target:
                    size = min(size, i - j)
                else:
                    break
                j+=1
                total-=nums[j]
                l2 = True
            if not l1 and not l2:
                break
        return 0 if size == float("inf") else size


        