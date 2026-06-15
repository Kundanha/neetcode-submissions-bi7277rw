class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rb = [len(heights)] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] <  heights[stack[-1]]:
                stack.pop() 
            if stack:
                rb[i] = stack[-1]
            stack.append(i)


        lb = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <=  heights[stack[-1]]:
                stack.pop() 
            if stack:
                lb[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(len(heights)):
            diff = rb[i] - lb[i] - 1
            area = heights[i] * diff
            maxArea = max(maxArea, area)
        return maxArea
