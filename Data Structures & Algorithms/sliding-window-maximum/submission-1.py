class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = -1
        j = -1
        res = []
        while True:
            l1 = False
            l2 = False

            while i < n-1 and i - j < k:
                i+=1
                l1 = True
                
            while j < i and i - j >= k:
                if i - j == k:
                    res.append(max(nums[j+1: i+1]))
                j+=1
                l2 = True
            
            if not l1 and not l2:
                break
        return res
        