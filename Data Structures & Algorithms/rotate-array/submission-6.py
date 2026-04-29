class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        r = n - k
        part1 = nums[:r][::-1]
        part2 = nums[r:][::-1]

        nums[:] = part1 + part2
        nums[:] = nums[::-1] 

        
        
        

        