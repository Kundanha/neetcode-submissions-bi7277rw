class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = -1
        j = -1
        num = 0
        length = float("inf")

        while True:
            l1 = False
            l2 = False
            while i < len(nums) - 1 and num < target:
                i+=1
                num += nums[i]
                l1 = True
            
            while j < i and num >= target:
                length = min(length, i-j)
                j+=1
                num -= nums[j]
                l2 = True
            if l1 == False and l2 == False:
                break
        return 0 if length == float("inf") else length
        