class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         l = 0
         r = len(nums) - 1
         resIndex = len(nums) - 1
         res = [0] * len(nums)
         while l<=r:
            if nums[l]**2 > nums[r] ** 2:
                res[resIndex] = nums[l]**2
                l+=1
                resIndex -=1
            else:
                res[resIndex] = nums[r]**2
                r-=1
                resIndex -=1

         return res