class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        i = 0
        while i < len(nums):
            j = i
            total = 0
            #while sum(nums[i:j+1]) <= goal:
            while j < len(nums):
                total += nums[j]
                if total == goal:
                    res+=1
                j+=1
            i+=1
        return res
            
            
        