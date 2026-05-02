class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        l = 0
        left = 0
        while l < n:
            left = max(left, height[l])
            leftMax[l] = left
            l+=1
        r = n - 1
        right = 0
        while r >= 0:
            right = max(right, height[r])
            rightMax[r] = right
            r-=1
        total = 0

        for i in range(n):
            h = min(leftMax[i], rightMax[i]) - height[i]
            total+=h
        return total

