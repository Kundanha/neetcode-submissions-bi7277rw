class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        total = 0
        for num in nums:
            total+=num
            if total - goal in mp:
                res+=mp[total - goal]
            mp[total]+=1
        return res
            

        