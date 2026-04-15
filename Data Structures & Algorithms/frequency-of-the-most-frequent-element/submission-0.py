class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()
        def bsearch(targetidx):
            l = 0
            r = targetidx
            res = targetidx
            while l <= r:
                mid = l + (r - l)//2
                count = targetidx - mid + 1
                windowSum = count * nums[targetidx]
                original = sum(nums[mid: targetidx+1])
                ops = windowSum - original
                if ops > k:
                    l = mid+1
                else:
                    res = mid
                    r = mid - 1
            return targetidx - res + 1
        for i in range(len(nums)):
            freq = bsearch(i)
            result = max(result, freq)
        return result


        