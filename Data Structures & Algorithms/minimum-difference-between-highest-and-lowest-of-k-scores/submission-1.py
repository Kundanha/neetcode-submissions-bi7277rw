class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = -1
        j = -1
        score = float("inf")

        while True:
            l1 = False
            l2 = False

            while i < len(nums) - 1 and i - j < k:
                i+=1
                l1 = True

            while  j < i and  i - j == k:
                #if i - j == k:
                    #score = min(score, nums[j+1: i+1][-1] - nums[j+1: i+1][0])
                score = min(score, nums[i] - nums[j + 1])
                j+=1
                l2 = True
                break
            if not l1 and not l2:
                break
        return score

        