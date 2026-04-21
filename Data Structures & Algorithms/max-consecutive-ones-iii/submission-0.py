class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = -1
        count = 0
        res = 0
        while i < len(nums):
            #aquire
            if nums[i] == 0:
                count+=1
                i+=1
            else:
                i+=1
            
            #if invalid, release until you are valid again
            while count> k:
                j+=1
                if nums[j] == 0:
                    count-=1
            if count <= k:
                res = max(res, i - j - 1) 

        return res


         