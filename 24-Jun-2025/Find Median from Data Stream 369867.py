# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heappush(self.left , -num)
        else:
            heappush(self.right , num)
        if len(self.left) > len(self.right) + 1:
            heappush(self.right , -(heappop(self.left)))
        elif len(self.right) > len(self.left) + 1:
            heappush(self.left , -(heappop(self.right)))


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -(self.left[0])
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (self.right[0] + -(self.left[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()