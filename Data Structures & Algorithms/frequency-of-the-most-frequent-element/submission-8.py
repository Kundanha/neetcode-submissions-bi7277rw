class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = -1
        j = -1
        ans = 0
        windowSum = 0

        while True:
            l1 = False
            l2 = False

            while i < len(nums) - 1:
                i+=1
                windowSum += nums[i]
                windowSize = i - j
                required = nums[i] * windowSize - windowSum
                if required <= k:
                    ans = max(ans, windowSize)
                    l1 = True
                else:
                    break
            while j < i:
                j+=1
                windowSum -= nums[j]
                windowSize = i - j
                required = nums[i] * windowSize - windowSum
                l2 = True
                if required <= k:
                    ans = max(ans, windowSize)
                    break
            if not l1 and not l2:
                break
        return ans


        