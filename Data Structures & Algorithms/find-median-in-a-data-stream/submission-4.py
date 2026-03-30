class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            mid1 = len(self.nums)//2
            mid2 = mid1-1
            return (self.nums[mid1]+self.nums[mid2])/2
        else:
            mid1 = len(self.nums)//2
            return  self.nums[mid1]
        
        