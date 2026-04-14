class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        numcount = 0
        i = -1
        j = -1
        windowSum = 0
        while True:
            l1 = False
            l2 = False
            
            while i < len(arr) - 1 and i - j < k:
                i+=1
                windowSum += arr[i]
                l1 = True
            while j < i and i - j == k:
                if i - j == k:
                    if windowSum // k >= threshold:
                        numcount+=1
                j+=1
                windowSum -= arr[j]
                l2 = True
                break
            if not l1 and not l2:
                break
        return numcount

        