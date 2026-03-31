class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i : i[0])

        prevEnd = intervals[0][1]

        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                result+=1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
                
        return result
        # hash map with 

        # iterate through each interval if overlap is more than 2 then add one
