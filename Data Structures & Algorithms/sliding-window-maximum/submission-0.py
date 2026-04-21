class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        res = []
        while i <= n - k:
            m = max(nums[i:i+k])
            res.append(m)
            i+=1
        return res

        