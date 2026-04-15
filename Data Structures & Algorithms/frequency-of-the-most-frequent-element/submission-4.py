class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
 
        def bsearch(targetidx):
            l = 0
            r = targetidx
            ans = targetidx
            while l <= r:
                mid = l + (r-l)//2
                count = (targetidx - mid) + 1
                windowSum = count * nums[targetidx]
                originalSum = prefix[targetidx+1] - prefix[mid]
                ops = windowSum - originalSum
                if ops>k:
                    l = mid+1
                else:
                    ans = mid
                    r = mid-1
            return targetidx - ans + 1
        for i in range(n):
            freq = bsearch(i)
            res = max(res, freq)
        return res
                
        