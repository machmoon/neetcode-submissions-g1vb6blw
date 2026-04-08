class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distance = []

        for x, y in points:
            heapq.heappush(distance, (math.sqrt(x*x+y*y), [x,y]))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(distance)[1])

        return result