class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        i = 0
        total = 1
        res = 1
        j = 1
        while j < len(nums):
            if nums[j]-nums[i] == 1:
                total+=1
                i+=1
                j+=1
            else:
                if nums[j] == nums[i]:
                    res = max(res, total)
                    i+=1
                    j+=1
                else:
                    res = max(res, total)
                    total = 1
                    i+=1
                    j+=1
        return max(res, total)

        