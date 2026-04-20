class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i = 0
        j = 0
        window = 0
        res = 0
        zerocount = 0
        while i < len(nums):
            window += nums[i]
            while j < i and (nums[j] == 0 or window > goal):
                if nums[j] == 0:
                    zerocount += 1
                else:
                    zerocount = 0
                window -= nums[j]
                j+=1
            if window == goal:
                res+=1 + zerocount
                
            i+=1
        return res
        

        