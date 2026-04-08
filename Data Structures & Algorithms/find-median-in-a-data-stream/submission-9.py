class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        # heapq.heappush(self.nums, num)
        self.nums.append(num)
        print(self.nums)

    def findMedian(self) -> float:
        
        n = len(self.nums)
        # self.data = heapq.heapify(self.nums)
        self.nums.sort()
        return (self.nums[n // 2] if (n & 1) else
                (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2)
        # if length == 0:
        #     return 

        # if length % 2 == 1:
        #     print(self.nums)
        #     return self.nums[length//2]
        # else:
        #     return (self.nums[length//2] + self.nums[length//2-1])/ 2
        
        