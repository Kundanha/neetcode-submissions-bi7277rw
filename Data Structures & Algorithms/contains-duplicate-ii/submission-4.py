class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = -1
        j = -1
        window = set()

        while True:
            l1 = False
            l2 = False
            while i<len(nums)-1:
                i+=1
                if nums[i] in window:
                    return True
                window.add(nums[i])
                l1 = True
                if i-j > k:
                    break
            while i - j > k:
                j += 1
                window.remove(nums[j])
                l2 = True
            if l1 == False and l2 == False:
                break
        return False


        