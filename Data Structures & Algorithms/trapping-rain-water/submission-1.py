class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        for i in range(n):
            left_max = max(height[0:i+1])
            right_max = max(height[i:n])
            smaller = min(left_max, right_max)
            total += smaller - height[i]
        return total
        