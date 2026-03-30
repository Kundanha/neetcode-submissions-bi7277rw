class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        length = len(self.nums)
        median = 0
        if length%2 == 0:
            half = (length//2)  - 1
            median = (self.nums[half] + self.nums[half + 1])/2 
        else:
            half = (length//2)
            median = self.nums[half]
        return median
        

        
        